import subprocess
import sys
from pathlib import Path


TESTS_DIR = Path(__file__).resolve().parent


def main():

    tests = sorted(
        p for p in TESTS_DIR.glob("test_*.py")
        if p.name != "test_mt5_connection.py"
    )

    print()
    print("=" * 70)
    print(" PROJECT PHOENIX AI - TEST SUITE COMPLETA")
    print("=" * 70)
    print()

    if not tests:

        print("NESSUN TEST TROVATO.")
        return 1

    print(f"Test trovati: {len(tests)}")
    print()

    for test in tests:
        print(f" - {test.name}")

    print()
    print("=" * 70)
    print(" AVVIO TEST COMPLETI")
    print("=" * 70)
    print()

    command = [
        sys.executable,
        "-m",
        "pytest",
        *[str(test) for test in tests],
        "-v"
    ]

    result = subprocess.run(command)

    print()
    print("=" * 70)
    print(" PROJECT PHOENIX AI - RISULTATO")
    print("=" * 70)
    print()

    if result.returncode == 0:

        print("TUTTI I TEST SONO PASSATI.")
        print()
        print("PROJECT PHOENIX AI")
        print("TEST SUITE: OK")
        print()

        return 0

    print("UNO O PIU' TEST SONO FALLITI.")
    print()
    print("PROJECT PHOENIX AI")
    print("TEST SUITE: FALLITA")
    print()

    return result.returncode


if __name__ == "__main__":
    sys.exit(main())
