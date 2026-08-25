from pathlib import Path
import ast

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.14 FULL INTEGRATION CONNECTION AUDIT")
print("=" * 100)

files = {
    "Analysis Engine":
        "Core/analysis_engine.py",

    "Market Analyzer":
        "Core/market_analyzer.py",

    "Smart Money":
        "Core/smart_money.py",

    "Phoenix Brain":
        "Core/phoenix_brain.py",

    "Signal Manager":
        "Core/signal_manager.py",

    "Risk Manager":
        "Core/risk_manager.py",

    "Trade Manager":
        "Core/trade_manager.py",

    "Live Trading Engine":
        "Core/live_trading_engine.py",

    "Execution Engine":
        "Execution/execution_engine.py",

    "Position Controller":
        "Core/position_controller.py",

    "Portfolio Manager":
        "Core/portfolio_manager.py",

    "Database":
        "Database/database_manager.py",
}

keywords = [
    "MarketAnalyzer",
    "SmartMoney",
    "PhoenixBrain",
    "SignalManager",
    "RiskManager",
    "TradeManager",
    "ExecutionEngine",
    "PositionController",
    "PortfolioManager",
    "DatabaseManager",
    "IndicatorManager",
    "analyze(",
    "evaluate(",
    "generate_trade(",
    "execute(",
    "open_position(",
    "close(",
    "save_trade(",
]

print()
print("=" * 100)
print("1. CONNECTION MAP")
print("=" * 100)

for name, raw_path in files.items():

    path = Path(raw_path)

    print()
    print("-" * 100)
    print(f"{name}")
    print(f"FILE: {raw_path}")
    print("-" * 100)

    if not path.exists():

        print("FILE NOT FOUND")
        continue

    text = path.read_text(
        encoding="utf-8-sig"
    )

    try:
        tree = ast.parse(text)
        print("SYNTAX: OK")
    except Exception as exc:
        print(
            f"SYNTAX: ERROR -> {exc}"
        )
        continue

    imports = []

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:
                imports.append(alias.name)

        elif isinstance(node, ast.ImportFrom):

            module = node.module or ""

            imports.append(module)

    print()
    print("IMPORTS:")
    for item in imports:
        print(f"  - {item}")

    print()
    print("RELEVANT CALLS / REFERENCES:")

    found = set()

    for number, line in enumerate(
        text.splitlines(),
        start=1
    ):

        for keyword in keywords:

            if keyword in line:

                value = (
                    number,
                    line.strip()
                )

                found.add(value)

    for number, line in sorted(found):

        print(
            f"  {number:04}: {line}"
        )

print()
print("=" * 100)
print("2. MAIN ORCHESTRATION CHECK")
print("=" * 100)

engine_path = Path(
    "Core/live_trading_engine.py"
)

if engine_path.exists():

    text = engine_path.read_text(
        encoding="utf-8-sig"
    )

    lines = text.splitlines()

    for number, line in enumerate(
        lines,
        start=1
    ):

        if any(
            key in line
            for key in [
                "self.analysis",
                "self.market",
                "self.smart",
                "self.brain",
                "self.signal",
                "self.risk",
                "self.trade",
                "self.execution",
                "self.position",
                "self.portfolio",
                "self.database",
            ]
        ):

            print(
                f"{number:04}: {line}"
            )

print()
print("=" * 100)
print("3. EXPECTED PIPELINE")
print("=" * 100)

pipeline = [
    "Market Data",
    "Indicators",
    "Market Analyzer",
    "Smart Money",
    "Phoenix Brain",
    "Signal Manager",
    "Risk Manager",
    "Trade Manager",
    "Execution Engine",
    "MT5",
    "Position Controller",
    "Portfolio Manager",
    "Database",
]

for index, item in enumerate(
    pipeline,
    start=1
):

    print(
        f"{index:02}. {item}"
    )

print()
print("=" * 100)
print("E.27.14 CONNECTION AUDIT COMPLETATO")
print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

