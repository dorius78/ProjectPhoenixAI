from Execution.execution_validator import ExecutionValidator

print("=" * 100)
print("PROJECT PHOENIX AI - E.27.58 EXECUTION VALIDATOR BEHAVIORAL TEST")
print("=" * 100)

validator = ExecutionValidator()

tests = [

    (
        "1. BUY VALIDO",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0.1
        },
        True
    ),

    (
        "2. SELL VALIDO",
        {
            "symbol": "BTC-USD",
            "signal": "SELL",
            "side": "SELL",
            "entry": 100000,
            "stop_loss": 101000,
            "take_profit": 98000,
            "atr": 1000,
            "size": 0.1
        },
        True
    ),

    (
        "3. NONE",
        None,
        False
    ),

    (
        "4. TRADE VUOTO",
        {},
        False
    ),

    (
        "5. ENTRY ZERO",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 0,
            "stop_loss": -1000,
            "take_profit": 2000,
            "atr": 1000,
            "size": 0.1
        },
        False
    ),

    (
        "6. ATR ZERO",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 0,
            "size": 0.1
        },
        False
    ),

    (
        "7. SIZE ZERO",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0
        },
        False
    ),

    (
        "8. SIGNAL SIDE INCOERENTI",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "SELL",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0.1
        },
        False
    ),

    (
        "9. BUY LIVELLI ERRATI",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 101000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0.1
        },
        False
    ),

    (
        "10. SELL LIVELLI ERRATI",
        {
            "symbol": "BTC-USD",
            "signal": "SELL",
            "side": "SELL",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0.1
        },
        False
    ),

    (
        "11. CAMPO MANCANTE",
        {
            "symbol": "BTC-USD",
            "signal": "BUY",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000
        },
        False
    ),

    (
        "12. SIGNAL INVALIDO",
        {
            "symbol": "BTC-USD",
            "signal": "INVALID",
            "side": "BUY",
            "entry": 100000,
            "stop_loss": 99000,
            "take_profit": 102000,
            "atr": 1000,
            "size": 0.1
        },
        False
    ),

]

print()
print("=" * 100)
print("RISULTATI")
print("=" * 100)

passed = 0
failed = 0

for name, trade, expected in tests:

    result, reason = validator.validate(trade)

    ok = result == expected

    if ok:
        passed += 1
    else:
        failed += 1

    print()
    print(name)
    print(f"  EXPECTED = {expected}")
    print(f"  RESULT   = {result}")
    print(f"  REASON   = {reason}")
    print(f"  CHECK    = {'PASS' if ok else 'FAIL'}")


print()
print("=" * 100)
print("SUMMARY")
print("=" * 100)

print(f"TEST TOTAL = {len(tests)}")
print(f"PASSED     = {passed}")
print(f"FAILED     = {failed}")

print()

if failed == 0:

    print("E.27.58 EXECUTION VALIDATOR: PASS")

else:

    print("E.27.58 EXECUTION VALIDATOR: ATTENTION")

print("=" * 100)
print("NESSUNA MODIFICA AL PRODUCTION CODE")
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

