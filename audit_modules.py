from pathlib import Path
import ast
import importlib.util

root = Path(".")

print()
print("=" * 70)
print(" PROJECT PHOENIX AI - CONTROLLO MODULI")
print("=" * 70)
print()

modules = set()

folders = [
    root / "Core",
    root / "Execution",
    root / "Database",
    root / "Data",
    root / "Config",
]

for folder in folders:

    if not folder.exists():
        continue

    for path in folder.rglob("*.py"):

        try:
            tree = ast.parse(
                path.read_text(encoding="utf-8")
            )

            for node in ast.walk(tree):

                if isinstance(node, ast.ImportFrom):

                    if node.module:
                        modules.add(node.module)

                elif isinstance(node, ast.Import):

                    for name in node.names:
                        modules.add(name.name)

        except Exception:
            pass


print("CONTROLLO MODULI LOCALI")
print("-" * 70)
print()

missing = []

local_prefixes = (
    "Core.",
    "Execution.",
    "Database.",
    "Data.",
    "Config.",
    "Logs.",
)

for module in sorted(modules):

    if not module.startswith(local_prefixes):
        continue

    spec = importlib.util.find_spec(module)

    if spec is None:

        print(f"[MANCANTE] {module}")
        missing.append(module)

    else:

        print(f"[ OK ]      {module}")


print()
print("=" * 70)
print(" RISULTATO")
print("=" * 70)
print()

if missing:

    print(f"MODULI MANCANTI: {len(missing)}")
    print()

    for module in missing:
        print(f" - {module}")

    print()
    print("AZIONE NECESSARIA: correggere le dipendenze mancanti.")

else:

    print("TUTTI I MODULI LOCALI RISULTANO PRESENTI.")

print()
