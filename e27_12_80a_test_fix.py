from pathlib import Path

path = Path(
    "e27_12_68_normal_close_result_lifecycle_test.py"
)

text = path.read_text(
    encoding="utf-8"
)

marker = '''    def save_trade(self, trade):
'''

method = '''    def has_trade(self, trade_id):

        if trade_id is None:

            return False

        for trade in self.saved:

            if str(
                trade.get(
                    "trade_id"
                )
            ) == str(trade_id):

                return True

        return False

'''

if marker not in text:
    raise RuntimeError(
        "STOP: metodo FakeDatabase.save_trade() non trovato"
    )

if "def has_trade(self, trade_id):" in text:
    raise RuntimeError(
        "STOP: FakeDatabase.has_trade() gia presente"
    )

text = text.replace(
    marker,
    method + marker,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.12.80A TEST FIX APPLICATO")
print("=" * 100)
print("Production code: NON MODIFICATO")
print("FakeDatabase.has_trade(): AGGIUNTO")
print("Idempotency test: PRONTO")
print("NESSUN ordine MT5")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

