"""
========================================
PROJECT PHOENIX AI
Supervisor / Devil's Advocate
Versione 1.0
========================================
"""

from Logs.logger import Logger


class Supervisor:

    def __init__(self):

        Logger.success(
            "Supervisor / Devil's Advocate V1 inizializzato."
        )

    # =====================================
    # SUPERVISIONE
    # =====================================

    def evaluate(
        self,
        decision,
        risk,
        regime,
        analysis
    ):

        reasons = []

        action = str(
            decision.get("action", "HOLD")
        ).upper()

        # =================================
        # HOLD
        # =================================

        if action == "HOLD":

            return {
                "decision": "BLOCK",
                "allowed": False,
                "reasons": ["Decisione HOLD"]
            }

        # =================================
        # RISK
        # =================================

        if not risk.get(
            "allow_trade",
            False
        ):

            reasons.append(
                "Risk Manager non autorizza il trade"
            )

        # =================================
        # REGIME
        # =================================

        regime_name = str(
            regime.get(
                "regime",
                "UNKNOWN"
            )
        ).upper()

        if regime_name == "SIDEWAYS":

            reasons.append(
                "Mercato laterale"
            )

        # =================================
        # QUALITÀ DECISIONE
        # =================================

        confidence = float(
            decision.get(
                "confidence",
                0
            )
        )

        if confidence < 30:

            reasons.append(
                "Confidence insufficiente"
            )

        # =================================
        # VERDETTO
        # =================================

        if reasons:

            return {
                "decision": "BLOCK",
                "allowed": False,
                "reasons": reasons
            }

        return {
            "decision": "ALLOW",
            "allowed": True,
            "reasons": [
                "Nessun veto Supervisor"
            ]
        }
        