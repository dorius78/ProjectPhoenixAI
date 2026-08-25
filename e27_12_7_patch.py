from pathlib import Path

path = Path("Core/live_trading_engine.py")
text = path.read_text(encoding="utf-8")

marker = "    # =====================================\n    # PREZZO CORRENTE\n    # =====================================\n"

if marker not in text:
    raise RuntimeError("STOP: punto di inserimento non trovato")

method = '''    # =====================================
    # SINCRONIZZAZIONE POSIZIONE MT5
    # =====================================

    def _sync_mt5_position(self):

        if self.position_controller.has_position():
            return False

        bridge = getattr(
            self.execution,
            "mt5",
            None
        )

        if bridge is None:
            return False

        get_positions = getattr(
            bridge,
            "get_phoenix_positions",
            None
        )

        if not callable(get_positions):
            return False

        try:
            positions = get_positions()
        except Exception as error:

            Logger.warning(
                "Sincronizzazione MT5 fallita: "
                f"{error}"
            )

            return False

        if not positions:
            return False

        position = positions[0]

        symbol = str(
            getattr(
                position,
                "symbol",
                "BTCUSD"
            )
        )

        position_type = int(
            getattr(
                position,
                "type",
                -1
            )
        )

        if position_type == 0:
            side = "BUY"
        elif position_type == 1:
            side = "SELL"
        else:
            Logger.warning(
                "Tipo posizione MT5 non riconosciuto."
            )
            return False

        entry = float(
            getattr(
                position,
                "price_open",
                0.0
            )
        )

        stop_loss = float(
            getattr(
                position,
                "sl",
                0.0
            )
        )

        take_profit = float(
            getattr(
                position,
                "tp",
                0.0
            )
        )

        size = float(
            getattr(
                position,
                "volume",
                0.0
            )
        )

        current_price = float(
            getattr(
                position,
                "price_current",
                entry
            )
        )

        ticket = int(
            getattr(
                position,
                "ticket",
                0
            )
        )

        magic = int(
            getattr(
                position,
                "magic",
                0
            )
        )

        if (
            ticket <= 0
            or entry <= 0
            or size <= 0
        ):
            Logger.warning(
                "Posizione MT5 non valida per "
                "la sincronizzazione."
            )
            return False

        if stop_loss <= 0 or take_profit <= 0:
            Logger.warning(
                "MT5: SL/TP non validi. "
                "Sincronizzazione ignorata."
            )
            return False

        opened = self.position_controller.open_position(
            side=side,
            entry=entry,
            stop_loss=stop_loss,
            take_profit=take_profit,
            symbol=symbol,
            size=size
        )

        if not opened:
            return False

        phoenix_position = (
            self.position_controller.get_position()
        )

        if phoenix_position is None:
            Logger.error(
                "Posizione Phoenix non disponibile "
                "dopo la sincronizzazione MT5."
            )
            return False

        phoenix_position["mt5_ticket"] = ticket
        phoenix_position["mt5_symbol"] = symbol
        phoenix_position["magic"] = magic
        phoenix_position["current_price"] = current_price

        if side == "BUY":
            phoenix_position["current_profit"] = float(
                getattr(
                    position,
                    "profit",
                    0.0
                )
            )
        else:
            phoenix_position["current_profit"] = float(
                getattr(
                    position,
                    "profit",
                    0.0
                )
            )

        Logger.success(
            "Posizione MT5 sincronizzata con Phoenix: "
            f"{symbol} #{ticket} {side}"
        )

        return True

'''

text = text.replace(
    marker,
    method + marker,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("E.27.12.7 MODIFICA APPLICATA")
