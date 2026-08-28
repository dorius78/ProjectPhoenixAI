from Logs.logger import Logger

from Core.phoenix_brain_logic import PhoenixBrainLogic


class PhoenixBrain:

    def __init__(self):

        Logger.success(
            "Phoenix Brain V11 inizializzato."
        )

        self.logic = PhoenixBrainLogic()

    # =====================================
    # DECISIONE
    # =====================================

    def think(
        self,
        analysis,
        risk,
        regime=None
    ):

        data = self.logic.calculate(
            analysis,
            risk,
            regime
        )

        score = float(
            data.get(
                "score",
                50
            )
        )

        confidence = float(
            data.get(
                "confidence",
                0
            )
        )

        bullish_score = float(
            data.get(
                "bullish_score",
                0
            )
        )

        bearish_score = float(
            data.get(
                "bearish_score",
                0
            )
        )

        dominant_direction = data.get(
            "dominant_direction",
            "NEUTRAL"
        )

        conflict = data.get(
            "conflict",
            False
        )

        # =================================
        # DECISION V2
        # =================================

        net_advantage = abs(
            bullish_score - bearish_score
        )

        action = "HOLD"

        # ---------------------------------
        # BUY
        # ---------------------------------

        if (
            dominant_direction == "BULLISH"
            and
            not conflict
            and
            net_advantage >= 15
            and
            confidence >= 30
        ):

            action = "BUY"

        # ---------------------------------
        # SELL
        # ---------------------------------

        elif (
            dominant_direction == "BEARISH"
            and
            not conflict
            and
            net_advantage >= 15
            and
            confidence >= 30
        ):

            action = "SELL"

        # ---------------------------------
        # STRONG BUY
        # ---------------------------------

        if (
            dominant_direction == "BULLISH"
            and
            not conflict
            and
            net_advantage >= 35
            and
            confidence >= 65
        ):

            action = "STRONG BUY"

        # ---------------------------------
        # STRONG SELL
        # ---------------------------------

        elif (
            dominant_direction == "BEARISH"
            and
            not conflict
            and
            net_advantage >= 35
            and
            confidence >= 65
        ):

            action = "STRONG SELL"

        # ---------------------------------
        # CONFLITTO
        # ---------------------------------

        if conflict:

            action = "HOLD"

        # ---------------------------------
        # CONFIDENCE MOLTO BASSA
        # ---------------------------------

        if confidence < 30:

            action = "HOLD"

        # ---------------------------------
        # RISK GATE
        # ---------------------------------

        if not risk.get(
            "allow_trade",
            False
        ):

            action = "HOLD"

        # =================================
        # OUTPUT
        # =================================

        return {

            "action": action,

            "score": score,

            "confidence": confidence,

            "strength": score,

            "risk": risk.get(
                "risk_level",
                "BASSO"
            ),

            "bullish_score": bullish_score,

            "bearish_score": bearish_score,

            "net_advantage": net_advantage,

            "dominant_direction":
                dominant_direction,

            "conflict": conflict,

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
