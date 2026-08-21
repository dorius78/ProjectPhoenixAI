"""
========================================
PROJECT PHOENIX AI
MT5 Broker
Versione 1.0

Connettore verso un broker reale via MetaTrader 5. Espone lo
stesso "contratto" del simulatore (Execution/execution_engine.py):
execute(trade) -> ordine, close(posizione_chiusa) -> report.

Questo permette al resto della pipeline (Core System, Live Trading
Engine, Position Controller) di non accorgersi della differenza:
non gli importa se dietro c'e' la simulazione o un broker vero.

IMPORTANTE:
- Richiede il pacchetto "MetaTrader5" (pip install MetaTrader5),
  disponibile SOLO su Windows, e il terminale MT5 installato e
  gia' collegato almeno una volta allo stesso account.
- Va testato PRIMA da solo (vedi Tests/test_mt5_connection.py)
  su un conto DEMO, mai direttamente nel ciclo di trading
  automatico.
========================================
"""

from datetime import datetime

from Logs.logger import Logger

try:

    import MetaTrader5 as mt5

    MT5_DISPONIBILE = True

except ImportError:

    MT5_DISPONIBILE = False


class MT5Broker:

    def __init__(self):

        if not MT5_DISPONIBILE:

            raise RuntimeError(
                "Il pacchetto 'MetaTrader5' non e' installato. "
                "Su Windows: pip install MetaTrader5"
            )

        from Config.mt5_credentials import (
            MT5_LOGIN,
            MT5_PASSWORD,
            MT5_SERVER,
            MT5_PATH,
            SYMBOL_MAP
        )

        self.login = MT5_LOGIN
        self.password = MT5_PASSWORD
        self.server = MT5_SERVER
        self.path = MT5_PATH
        self.symbol_map = SYMBOL_MAP

        self.connected = False

        Logger.success("MT5 Broker V1 inizializzato.")

    # =====================================
    # CONNESSIONE
    # =====================================

    def connect(self):

        kwargs = {}

        if self.path:
            kwargs["path"] = self.path

        if self.login:
            kwargs["login"] = int(self.login)

        if self.password:
            kwargs["password"] = self.password

        if self.server:
            kwargs["server"] = self.server

        if not mt5.initialize(**kwargs):

            code, description = mt5.last_error()

            Logger.warning(
                f"Connessione MT5 fallita: [{code}] {description}"
            )

            return False

        account = mt5.account_info()

        if account is None:

            Logger.warning(
                "Connesso al terminale MT5 ma nessun account attivo."
            )

            mt5.shutdown()

            return False

        self.connected = True

        Logger.success(
            f"MT5 connesso: conto {account.login} su "
            f"{account.server} | Saldo: {account.balance} "
            f"{account.currency}"
        )

        return True

    def disconnect(self):

        if self.connected:

            mt5.shutdown()

            self.connected = False

            Logger.info("MT5 disconnesso.")

    def get_balance(self):

        if not self.connected:

            return None

        account = mt5.account_info()

        if account is None:

            return None

        return round(account.balance, 2)

    # =====================================
    # TRADUZIONE SIMBOLO E VOLUME
    # =====================================

    def _mt5_symbol(self, symbol):

        # La ricerca ignora maiuscole/minuscole: "btc-usd",
        # "BTC-USD" e "Btc-Usd" devono risolversi allo stesso
        # simbolo del broker.
        for key, value in self.symbol_map.items():

            if key.upper() == symbol.upper():

                return value

        return symbol

    def _to_volume(self, mt5_symbol, size):

        info = mt5.symbol_info(mt5_symbol)

        if info is None:

            Logger.warning(
                f"Simbolo {mt5_symbol} non trovato su MT5."
            )

            return None

        if not info.visible:

            mt5.symbol_select(mt5_symbol, True)

        contract_size = info.trade_contract_size or 1.0

        volume = float(size) / float(contract_size)

        step = info.volume_step or 0.01

        volume = round(volume / step) * step

        volume = max(info.volume_min, min(volume, info.volume_max))

        return round(volume, 2)

    # =====================================
    # APERTURA ORDINE
    # =====================================

    def execute(self, trade):

        if not self.connected:

            Logger.warning("MT5 non connesso: impossibile eseguire.")

            return {"success": False, "reason": "MT5 non connesso"}

        symbol = self._mt5_symbol(trade["symbol"])

        volume = self._to_volume(symbol, trade.get("size", 1.0))

        if not volume or volume <= 0:

            return {"success": False, "reason": "Volume non valido"}

        tick = mt5.symbol_info_tick(symbol)

        if tick is None:

            Logger.warning(f"Nessun prezzo disponibile per {symbol}.")

            return {"success": False, "reason": "Nessun prezzo"}

        side = trade["side"]

        order_type = mt5.ORDER_TYPE_BUY if side == "BUY" else mt5.ORDER_TYPE_SELL

        price = tick.ask if side == "BUY" else tick.bid

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": volume,
            "type": order_type,
            "price": price,
            "sl": float(trade["stop_loss"]),
            "tp": float(trade["take_profit"]),
            "deviation": 20,
            "magic": 234000,
            "comment": "Phoenix AI",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)

        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:

            code = result.retcode if result else None

            comment = result.comment if result else "nessuna risposta"

            Logger.warning(
                f"Ordine MT5 rifiutato: [{code}] {comment}"
            )

            return {
                "success": False,
                "reason": f"[{code}] {comment}"
            }

        Logger.success(
            f"Ordine MT5 eseguito: {side} {symbol} "
            f"{volume} lotti @ {result.price}"
        )

        return {
            "success": True,
            "symbol": trade["symbol"],
            "side": side,
            "entry": float(result.price),
            "stop_loss": float(trade["stop_loss"]),
            "take_profit": float(trade["take_profit"]),
            "size": trade.get("size", 1.0),
            "mt5_ticket": result.order,
            "mt5_symbol": symbol,
            "mt5_volume": volume
        }

    # =====================================
    # CHIUSURA ORDINE
    # =====================================

    def close(self, closed_position):

        if not self.connected:

            Logger.warning("MT5 non connesso: impossibile chiudere.")

            return None

        mt5_symbol = closed_position.get(
            "mt5_symbol",
            self._mt5_symbol(closed_position["symbol"])
        )

        positions = mt5.positions_get(symbol=mt5_symbol)

        if not positions:

            Logger.warning(
                f"Nessuna posizione MT5 aperta trovata su {mt5_symbol}."
            )

            return {
                "symbol": closed_position["symbol"],
                "side": closed_position["side"],
                "entry": closed_position["entry"],
                "exit": closed_position["current_price"],
                "pnl": closed_position["current_profit"],
                "reason": closed_position["close_reason"],
                "close_time": closed_position.get("close_time") or datetime.now()
            }

        position = positions[0]

        tick = mt5.symbol_info_tick(mt5_symbol)

        is_buy = position.type == mt5.ORDER_TYPE_BUY

        close_type = mt5.ORDER_TYPE_SELL if is_buy else mt5.ORDER_TYPE_BUY

        price = tick.bid if is_buy else tick.ask

        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": mt5_symbol,
            "volume": position.volume,
            "type": close_type,
            "position": position.ticket,
            "price": price,
            "deviation": 20,
            "magic": 234000,
            "comment": "Phoenix AI Close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }

        result = mt5.order_send(request)

        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:

            code = result.retcode if result else None

            comment = result.comment if result else "nessuna risposta"

            Logger.warning(
                f"Chiusura MT5 fallita: [{code}] {comment}"
            )

            return None

        pnl = position.profit

        Logger.success(
            f"Posizione MT5 chiusa: {mt5_symbol} PnL {pnl:.2f}"
        )

        return {
            "symbol": closed_position["symbol"],
            "side": closed_position["side"],
            "entry": closed_position["entry"],
            "exit": float(result.price),
            "pnl": float(pnl),
            "reason": closed_position["close_reason"],
            "close_time": datetime.now()
        }