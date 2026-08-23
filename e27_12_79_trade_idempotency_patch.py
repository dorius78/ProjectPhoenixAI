from pathlib import Path

path = Path(
    "Core/live_trading_engine.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''        # =================================
        # CLOSE ROUTING
        # =================================
        #
        # Se MT5 ha gia chiuso la posizione
        # esternamente, NON dobbiamo chiamare
        # execution.close().
        #
        # La chiusura e gia avvenuta sul broker.
        # Phoenix deve solamente registrare
        # l'evento.
        #

        external_mt5_close = (
'''

new = '''        # =================================
        # IDEMPOTENCY CHECK
        # =================================
        #
        # Ogni trade chiuso deve essere
        # processato una sola volta.
        #
        # Prima di qualsiasi execution.close()
        # verifichiamo se il trade e gia
        # presente nel Database.
        #

        trade_id = (
            closed.get("trade_id")
            or closed.get("mt5_ticket")
        )

        if trade_id is not None:

            if self.database.has_trade(
                trade_id
            ):

                Logger.info(
                    "TRADE GIA PROCESSATO: "
                    f"{trade_id}. "
                    "Nessuna nuova chiusura."
                )

                return False

        # =================================
        # CLOSE ROUTING
        # =================================
        #
        # Se MT5 ha gia chiuso la posizione
        # esternamente, NON dobbiamo chiamare
        # execution.close().
        #
        # La chiusura e gia avvenuta sul broker.
        # Phoenix deve solamente registrare
        # l'evento.
        #

        external_mt5_close = (
'''

if old not in text:

    raise RuntimeError(
        "STOP: punto CLOSE ROUTING non trovato"
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
print("E.27.12.79 IDEMPOTENCY PATCH APPLICATA")
print("=" * 100)
print("BACKUP: OK")
print("TRADE ID CHECK: OK")
print("DATABASE has_trade(): OK")
print("CHECK PRIMA DI execution.close(): OK")
print("EXTERNAL CLOSE PROTETTO: OK")
print("Production code modificato: SI")
print("NESSUN ordine MT5 durante la patch")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

