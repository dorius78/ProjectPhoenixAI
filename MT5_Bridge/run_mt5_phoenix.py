"""
PROJECT PHOENIX AI
MT5 -> PHOENIX READ-ONLY TEST
"""

from mt5_bridge import MT5DataBridge


def main():
    bridge = MT5DataBridge(symbol="EURUSD", timeframe="M5")

    print("=" * 70)
    print(" PROJECT PHOENIX AI - MT5 DATA TEST")
    print("=" * 70)

    if not bridge.connect():
        print("ERRORE: impossibile collegarsi a MT5.")
        return 1

    try:
        snapshot = bridge.snapshot(50)

        print(f"MT5: CONNESSO")
        print(f"SIMBOLO: {snapshot['symbol']}")
        print(f"TIMEFRAME: {snapshot['timeframe']}")
        print(f"BID: {snapshot['tick']['bid']}")
        print(f"ASK: {snapshot['tick']['ask']}")
        print(f"CANDELE RICEVUTE: {len(snapshot['candles'])}")
        print(f"ORDINI ABILITATI: {snapshot['execution_enabled']}")

        if snapshot["candles"]:
            last = snapshot["candles"][-1]
            print(
                "ULTIMA CANDELA:",
                f"O={last['open']} H={last['high']} "
                f"L={last['low']} C={last['close']}"
            )

        print("=" * 70)
        print(" MT5 DATA BRIDGE: SUPERATO")
        print("=" * 70)
        return 0

    finally:
        bridge.disconnect()


if __name__ == "__main__":
    raise SystemExit(main())
