import subprocess
import sys

ROOT = r"C:\ProjectPhoenixAI"

tests = [
    "Tests.test_demo_safety_gate",
    "Tests.test_indicators",
    "Tests.test_risk",
    "Tests.test_signal",
    "Tests.test_trade_builder",
    "Tests.test_trading_guard",
]

print("=" * 100)
print("PROJECT PHOENIX AI - REGRESSION GATE V2")
print("=" * 100)

failed = []

for test in tests:
    print("")
    print("-" * 100)
    print("RUN:", test)
    print("-" * 100)

    result = subprocess.run(
        [sys.executable, "-m", test],
        cwd=ROOT
    )

    if result.returncode == 0:
        print("PASS:", test)
    else:
        print("FAIL:", test)
        failed.append(test)

print("")
print("=" * 100)

if failed:
    print("REGRESSION GATE = FAIL")
    print("TEST FALLITI:")
    for test in failed:
        print(" -", test)
else:
    print("REGRESSION GATE = PASS")
    print("TEST ESEGUITI =", len(tests))
    print("FAIL = 0")

print("")
print("NESSUN ORDER_SEND")
print("NESSUN ORDINE MT5")
print("NESSUN LIVE")
print("=" * 100)

sys.exit(1 if failed else 0)
