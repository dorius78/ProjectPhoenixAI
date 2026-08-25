from pathlib import Path

path = Path("Core/live_trading_engine.py")

text = path.read_text(
    encoding="utf-8"
)

old = '''        if self.position_controller.has_position():
            return False
'''

new = '''        # =================================
        # POSIZIONE PHOENIX GIA APERTA
        # =================================
        #
        # In questo caso controlliamo anche
        # se la posizione MT5 è ancora presente.
        #
        # Se MT5 l'ha chiusa esternamente,
        # Phoenix deve registrare la chiusura
        # senza inviare un nuovo order_send().
        #

        phoenix_has_position = (
            self.position_controller.has_position()
        )

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

        # =================================
        # POSIZIONE MT5 SCOMPARSA
        # =================================

        if (
            phoenix_has_position
            and not positions
        ):

            position = (
                self.position_controller.get_position()
            )

            if position is None:
                return False

            from datetime import datetime

            closed = position.copy()

            closed["status"] = "CLOSED"

            closed["close_reason"] = (
                "MT5 EXTERNAL CLOSE"
            )

            closed["close_time"] = datetime.now()

            closed["current_price"] = float(
                position.get(
                    "current_price",
                    position.get(
                        "entry",
                        0.0
                    )
                )
            )

            closed["current_profit"] = float(
                position.get(
                    "current_profit",
                    0.0
                )
            )

            closed["mt5_ticket"] = int(
                position.get(
                    "mt5_ticket",
                    0
                )
                or 0
            )

            # =================================
            # RESET POSITION CONTROLLER
            # =================================

            self.position_controller.reset()

            Logger.success(
                "MT5: posizione scomparsa. "
                "Chiusura esterna sincronizzata "
                "con Phoenix."
            )

            # =================================
            # PROCESS CLOSED TRADE
            # =================================

            processed = (
                self._process_closed_position(
                    closed
                )
            )

            if not processed:

                Logger.warning(
                    "Chiusura MT5 rilevata ma "
                    "processamento trade non completato."
                )

            return processed

        # =================================
        # PHOENIX NON HA POSIZIONE
        # =================================

        if not positions:
            return False

        # =================================
        # POSIZIONE MT5 DA SINCRONIZZARE
        # =================================

        if phoenix_has_position:
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

        if (
            stop_loss <= 0
            or take_profit <= 0
        ):

            Logger.warning(
                "MT5: SL/TP non validi. "
                "Sincronizzazione ignorata."
            )

            return False

        opened = (
            self.position_controller.open_position(

                side=side,

                entry=entry,

                stop_loss=stop_loss,

                take_profit=take_profit,

                symbol=symbol,

                size=size

            )
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

        phoenix_position["current_price"] = (
            current_price
        )

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

if old not in text:
    raise RuntimeError(
        "STOP: blocco iniziale _sync_mt5_position() non trovato"
    )

# Evita doppia applicazione
if "MT5 EXTERNAL CLOSE" in text:
    raise RuntimeError(
        "STOP: patch E.27.12.37 gia presente"
    )

text = text.replace(
    old,
    new,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.12.37 PATCH APPLICATA")
print("=" * 100)
print("MT5 EXTERNAL CLOSE: OK")
print("CLOSED PAYLOAD: OK")
print("POSITION CONTROLLER RESET: OK")
print("PROCESS CLOSED TRADE: OK")
print("NESSUN order_send")
print("NESSUNA apertura MT5")
print("NESSUNA chiusura MT5")
print("=" * 100)

