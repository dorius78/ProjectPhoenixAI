from pathlib import Path

path = Path(
    "Core/signal_manager.py"
)

text = path.read_text(
    encoding="utf-8-sig"
)

patches = [

    (
        '''            elif signal == "STRONG BUY":

                if dominant_direction != "BULLISH":
''',
        '''            elif signal == "STRONG BUY":

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BULLISH":
'''
    ),

    (
        '''            elif signal == "STRONG SELL":

                if dominant_direction != "BEARISH":
''',
        '''            elif signal == "STRONG SELL":

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BEARISH":
'''
    ),

]

print("=" * 100)
print("E.27.47 STRONG SIGNAL CONFIDENCE GATE PATCH")
print("=" * 100)

for number, (old, new) in enumerate(
    patches,
    start=1
):

    count = text.count(old)

    print(
        f"PATCH {number}: occurrences = {count}"
    )

    if count != 1:

        raise RuntimeError(
            f"STOP PATCH {number}: "
            "blocco non trovato in modo univoco."
        )

    text = text.replace(
        old,
        new,
        1
    )

path.write_text(
    text,
    encoding="utf-8"
)

print()
print("PATCH APPLICATA: OK")
print()
print("STRONG BUY MIN_CONFIDENCE: FIX")
print("STRONG SELL MIN_CONFIDENCE: FIX")
print("BUY MIN_CONFIDENCE: INVARIATO")
print("SELL MIN_CONFIDENCE: INVARIATO")
print("MIN_CONFIDENCE: 60")
print("CONFLICT LOGIC: INVARIATA")
print("DIRECTION LOGIC: INVARIATA")
print("RISK AI: INVARIATO")
print("MT5: INVARIATO")
print()
print("NESSUN ORDINE MT5")
print("NESSUNA APERTURA")
print("NESSUNA CHIUSURA")
print("=" * 100)

