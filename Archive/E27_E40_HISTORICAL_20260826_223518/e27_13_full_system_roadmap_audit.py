from pathlib import Path
import ast

files = {
    "Live Trading Engine": Path("Core/live_trading_engine.py"),
    "Execution Engine": Path("Execution/execution_engine.py"),
    "MT5 Bridge": Path("MT5_Bridge/mt5_execution_recovered.py"),
    "Position Controller": Path("Core/position_controller.py"),
    "Portfolio Manager": Path("Core/portfolio_manager.py"),
    "Risk Manager": Path("Core/risk_manager.py"),
    "Trade Manager": Path("Core/trade_manager.py"),
    "Analysis Engine": Path("Core/analysis_engine.py"),
    "Database": Path("Database/database_manager.py"),
}

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.13 FULL SYSTEM ROADMAP AUDIT")
print("=" * 100)

for name, path in files.items():

    print()
    print("=" * 100)
    print(name)
    print(path)
    print("=" * 100)

    if not path.exists():
        print("FILE: NOT FOUND")
        continue

    text = path.read_text(
        encoding="utf-8"
    )

    print(
        f"LINES: {len(text.splitlines())}"
    )

    try:
        tree = ast.parse(text)
        print("SYNTAX: OK")
    except Exception as exc:
        print("SYNTAX: ERROR")
        print(exc)
        continue

    classes = []
    functions = []

    for node in ast.walk(tree):

        if isinstance(node, ast.ClassDef):
            classes.append(node.name)

        elif isinstance(
            node,
            (
                ast.FunctionDef,
                ast.AsyncFunctionDef,
            )
        ):
            functions.append(node.name)

    print()
    print("CLASSES:")
    for item in sorted(set(classes)):
        print(f"  - {item}")

    print()
    print("METHODS / FUNCTIONS:")
    for item in sorted(set(functions)):
        print(f"  - {item}")

print()
print("=" * 100)
print("E.27.13 ROADMAP COMPONENT CHECK")
print("=" * 100)

checks = {
    "Market Intelligence":
        [
            "Core/market_analyzer.py",
            "Core/smart_money.py",
        ],

    "Technical AI":
        [
            "Indicators/indicator_manager.py",
        ],

    "Decision AI":
        [
            "Core/phoenix_brain.py",
            "Core/signal_manager.py",
        ],

    "Risk AI":
        [
            "Core/risk_manager.py",
            "Core/trading_guard.py",
        ],

    "Trade Lifecycle":
        [
            "Core/trade_manager.py",
            "Core/position_controller.py",
            "Core/portfolio_manager.py",
        ],

    "Execution":
        [
            "Execution/execution_engine.py",
            "MT5_Bridge/mt5_execution_recovered.py",
        ],

    "Database":
        [
            "Database/database_manager.py",
        ],

    "Backtest":
        [
            "Backtest",
        ],

    "News Intelligence":
        [
            "News",
        ],

    "Sentiment AI":
        [
            "Sentiment",
        ],
}

for component, paths in checks.items():

    found = []

    for raw in paths:

        path = Path(raw)

        if path.exists():
            found.append(raw)

    if found:
        print(
            f"[ PRESENT ] {component}"
        )
        for item in found:
            print(
                f"             {item}"
            )
    else:
        print(
            f"[ MISSING  ] {component}"
        )

print()
print("=" * 100)
print("GIT CHECKPOINT")
print("=" * 100)
print("Checkpoint atteso: e0a9db7")
print("=" * 100)

print()
print("E.27.13 AUDIT COMPLETATO")
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

