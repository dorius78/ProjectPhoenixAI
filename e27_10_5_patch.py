from pathlib import Path

path = Path("Execution/mt5_broker.py")
text = path.read_text(encoding="utf-8")

old = "    def execute(self, trade):"
new = "    def execute(self, trade, dry_run=False):"

if old not in text:
    raise RuntimeError("STOP: firma execute() non trovata")

if new in text:
    raise RuntimeError("STOP: modifica gia presente")

text = text.replace(old, new, 1)

marker = "        if not self.connected:"

start = text.index(new)
pos = text.index(marker, start)

insertion = """        if dry_run:

            Logger.info(
                "MT5 DRY RUN: nessun ordine inviato."
            )

            return {
                "success": False,
                "executed": False,
                "dry_run": True,
                "reason": "DRY RUN attivo"
            }

"""

text = text[:pos] + insertion + text[pos:]

path.write_text(text, encoding="utf-8")

print("E.27.10.5 MODIFICA APPLICATA")
