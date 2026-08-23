from pathlib import Path

path = Path("Core/live_trading_engine.py")
lines = path.read_text(encoding="utf-8").splitlines()

# Cerchiamo il while True del metodo start()
start_index = None

for i, line in enumerate(lines):

    if line.strip().startswith("def start("):
        for j in range(i + 1, min(i + 40, len(lines))):
            if lines[j].strip() == "while True:":
                start_index = j
                break
        break

if start_index is None:
    raise RuntimeError(
        "STOP: while True di start() non trovato"
    )

# Controllo anti-duplicazione
end_check = min(
    start_index + 25,
    len(lines)
)

for i in range(start_index, end_check):

    if "_sync_mt5_position()" in lines[i]:
        raise RuntimeError(
            "STOP: sincronizzazione gia presente"
        )

insertion = [
    "",
    "                # =================================",
    "                # SINCRONIZZAZIONE MT5",
    "                # =================================",
    "",
    "                self._sync_mt5_position()",
    ""
]

# Inseriamo subito dopo while True:
lines[start_index + 1:start_index + 1] = insertion

path.write_text(
    "\n".join(lines) + "\n",
    encoding="utf-8"
)

print(
    "E.27.12.10 MODIFICA APPLICATA"
)
print(
    "Inserita sincronizzazione dopo "
    f"while True alla riga originale {start_index + 1}"
)
