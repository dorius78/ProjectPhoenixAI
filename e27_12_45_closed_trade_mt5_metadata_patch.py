from pathlib import Path

path = Path("Core/live_trading_engine.py")

text = path.read_text(
    encoding="utf-8"
)

old = '''            "trade_id":
                trade_id,

            "symbol":
                symbol,

            "side":
                side,
'''

new = '''            "trade_id":
                trade_id,

            # =================================
            # METADATI MT5
            # =================================

            "mt5_ticket":
                closed.get(
                    "mt5_ticket",
                    report.get(
                        "mt5_ticket",
                        0
                    )
                ),

            "mt5_symbol":
                closed.get(
                    "mt5_symbol",
                    report.get(
                        "mt5_symbol",
                        symbol
                    )
                ),

            "magic":
                closed.get(
                    "magic",
                    report.get(
                        "magic",
                        0
                    )
                ),

            "mt5_order_ticket":
                closed.get(
                    "mt5_order_ticket",
                    report.get(
                        "order_ticket",
                        0
                    )
                ),

            "mt5_deal_ticket":
                closed.get(
                    "mt5_deal_ticket",
                    report.get(
                        "deal_ticket",
                        0
                    )
                ),

            "symbol":
                symbol,

            "side":
                side,
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco trade_id del trade finale non trovato"
    )

if '"mt5_order_ticket":' in text:
    raise RuntimeError(
        "STOP: metadati MT5 gia presenti"
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
print("E.27.12.45 PATCH APPLICATA")
print("=" * 100)
print("mt5_ticket: OK")
print("mt5_symbol: OK")
print("magic: OK")
print("mt5_order_ticket: OK")
print("mt5_deal_ticket: OK")
print("NESSUN order_send")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

