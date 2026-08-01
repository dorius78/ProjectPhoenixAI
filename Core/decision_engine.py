"""
========================================
PROJECT PHOENIX AI
Decision Engine
Versione 7.0
========================================
"""

from Core.phoenix_score import PhoenixScore
from Logs.logger import Logger


class DecisionEngine:

    def __init__(self):

        self.score_engine = PhoenixScore()

        self.last_decision = None

        Logger.success("Decision Engine V7 inizializzato.")

    # =====================================
    # ANALISI DECISIONE
    # =====================================

    def analyze(self, analysis):

        result = self.score_engine.calculate(analysis)

        self.last_decision = {

            "signal": result["signal"],

            "score": result["score"],

            "confidence": result["confidence"],

            "direction_score": result.get(
                "direction_score",
                result["score"]
            ),

            "reasons": result["reasons"].copy(),

            "analysis": analysis

        }

        return self.last_decision

    # =====================================
    # CONTROLLI
    # =====================================

    def is_buy(self):

        if self.last_decision is None:
            return False

        return self.last_decision["signal"] in (
            "BUY",
            "STRONG BUY"
        )

    def is_sell(self):

        if self.last_decision is None:
            return False

        return self.last_decision["signal"] in (
            "SELL",
            "STRONG SELL"
        )

    def is_hold(self):

        if self.last_decision is None:
            return True

        return self.last_decision["signal"] == "HOLD"

    # =====================================
    # REPORT
    # =====================================

    def summary(self):

        if self.last_decision is None:

            Logger.warning("Nessuna decisione disponibile.")

            return

        Logger.separator()

        Logger.title("DECISION ENGINE")

        Logger.info(
            f"Segnale      : {self.last_decision['signal']}"
        )

        Logger.info(
            f"Score        : {self.last_decision['score']}"
        )

        Logger.info(
            f"Confidence   : {self.last_decision['confidence']:.2f}"
        )

        Logger.blank()

        Logger.info("Motivazioni:")

        for reason in self.last_decision["reasons"]:

            Logger.info(f"✔ {reason}")

        Logger.separator()

    # =====================================
    # EXPORT
    # =====================================

    def export(self):

        if self.last_decision is None:
            return None

        return self.last_decision.copy()

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.last_decision = None

        Logger.info("Decision Engine resettato.")