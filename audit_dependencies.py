from pathlib import Path
import ast

root = Path(".")

folders = [
    root / "Core",
    root / "Execution",
    root / "Database",
]

print()
print("=" * 70)
print(" PROJECT PHOENIX AI - AUDIT DIPENDENZE")
print("=" * 70)
print()

for folder in folders:

    if not folder.exists():
        continue

    print()
    print(f"[{folder.name}]")
    print("-" * 70)

    for path in sorted(folder.glob("*.py")):

        print()
        print(path)

        try:
            tree = ast.parse(
                path.read_text(encoding="utf-8")
            )

            imports = []

            for node in ast.walk(tree):

                if isinstance(node, ast.ImportFrom):

                    if node.module:
                        imports.append(node.module)

                elif isinstance(node, ast.Import):

                    for name in node.names:
                        imports.append(name.name)

            for module in sorted(set(imports)):
                print(f"   -> {module}")

        except Exception as error:

            print(f"   !! ERRORE LETTURA: {error}")

print()
print("=" * 70)
print(" AUDIT COMPLETATO")
print("=" * 70)
print()
