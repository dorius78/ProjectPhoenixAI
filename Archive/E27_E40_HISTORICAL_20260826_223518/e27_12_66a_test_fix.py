from pathlib import Path

path = Path(
    "e27_12_66_external_close_no_reopen_safety_test.py"
)

text = path.read_text(
    encoding="utf-8"
)

old = '''    def update_balance(self, pnl):

        print(
            f"[PORTFOLIO] update_balance({pnl})"
        )

        self.balance += pnl

    def remove(self, symbol):
'''

new = '''    def update_balance(self, pnl):

        print(
            f"[PORTFOLIO] update_balance({pnl})"
        )

        self.balance += pnl

    def get_balance(self):

        return self.balance

    def remove(self, symbol):
'''

if old not in text:
    raise RuntimeError(
        "STOP: blocco FakePortfolio non trovato"
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
print("E.27.12.66A TEST FIX APPLICATO")
print("=" * 100)
print("Production code: NON MODIFICATO")
print("FakePortfolio.get_balance(): AGGIUNTO")
print("NESSUN order_send")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

