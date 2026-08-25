from Logs.logger import Logger

from Core.phoenix_brain_logic import PhoenixBrainLogic


class PhoenixBrain:

    def __init__(self):

        Logger.success(
            "Phoenix Brain V10 inizializzato."
        )

        self.logic = PhoenixBrainLogic()

    # =====================================
    # DECISIONE
    # =====================================

    def think(
        self,
        analysis,
        risk
    ):

        data = self.logic.calculate(
            analysis,
            risk
        )

        score = data["score"]

        # =================================
        # AZIONE
        # =================================

        if score >= 90:

            action = "STRONG BUY"

        elif score >= 70:

            action = "BUY"

        elif score <= 10:

            action = "STRONG SELL"

        elif score <= 30:

            action = "SELL"

        else:

            action = "HOLD"

        # =================================
        # OUTPUT COMPLETO
        # =================================

        return {

            "action": action,

            "score": score,

            "confidence": data["confidence"],

            "strength": score,

            "risk": risk["risk_level"],

            # =============================
            # DIREZIONE
            # =============================

            "bullish_score": data.get(
                "bullish_score",
                0
            ),

            "bearish_score": data.get(
                "bearish_score",
                0
            ),

            "dominant_direction": data.get(
                "dominant_direction",
                "NEUTRAL"
            ),

            "conflict": data.get(
                "conflict",
                False
            ),

            # =============================
            # SPIEGAZIONE
            # =============================

            "reasons": data.get(
                "reasons",
                []
            ),

            "warnings": data.get(
                "warnings",
                []
            ),

            "bullish_reasons": data.get(
                "bullish_reasons",
                []
            ),

            "bearish_reasons": data.get(
                "bearish_reasons",
                []
            )

        }