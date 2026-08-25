from Config.settings import MIN_CONFIDENCE
from Logs.logger import Logger


class SignalManager:

    def __init__(self):

        Logger.success(
            "Signal Manager V10 inizializzato."
        )

    # =====================================
    # VALIDAZIONE
    # =====================================

    def validate(self, decision):

        signal = str(
            decision.get(
                "action",
                "HOLD"
            )
        ).upper()

        confidence = float(
            decision.get(
                "confidence",
                0
            )
        )

        score = int(
            decision.get(
                "score",
                0
            )
        )

        dominant_direction = str(
            decision.get(
                "dominant_direction",
                "NEUTRAL"
            )
        ).upper()

        conflict = bool(
            decision.get(
                "conflict",
                False
            )
        )

        reasons = decision.get(
            "reasons",
            []
        )

        warnings = decision.get(
            "warnings",
            []
        )

        bullish_score = float(
            decision.get(
                "bullish_score",
                0
            )
        )

        bearish_score = float(
            decision.get(
                "bearish_score",
                0
            )
        )

        valid = False

        rejection_reason = None

        # =================================
        # HOLD
        # =================================

        if signal == "HOLD":

            rejection_reason = (
                "Brain ha generato HOLD."
            )

        # =================================
        # SEGNALI OPERATIVI
        # =================================

        elif signal in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL"
        ):

            # -----------------------------
            # CONFLITTO
            # -----------------------------

            if conflict:

                rejection_reason = (
                    "Segnale bloccato: "
                    "conflitto tra direzioni."
                )

            # =================================
            # STRONG BUY
            # =================================

            elif signal == "STRONG BUY":

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BULLISH":

                    rejection_reason = (
                        "Direzione dominante "
                        "non rialzista."
                    )

                else:

                    valid = True

            # =================================
            # STRONG SELL
            # =================================

            elif signal == "STRONG SELL":

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BEARISH":

                    rejection_reason = (
                        "Direzione dominante "
                        "non ribassista."
                    )

                else:

                    valid = True

            # =================================
            # BUY
            # =================================

            elif signal == "BUY":

                # BUY normale richiede
                # la confidence minima.

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BULLISH":

                    rejection_reason = (
                        "Direzione dominante "
                        "non rialzista."
                    )

                else:

                    valid = True

            # =================================
            # SELL
            # =================================

            elif signal == "SELL":

                # SELL normale richiede
                # la confidence minima.

                if confidence < MIN_CONFIDENCE:

                    rejection_reason = (
                        "Confidence insufficiente."
                    )

                elif dominant_direction != "BEARISH":

                    rejection_reason = (
                        "Direzione dominante "
                        "non ribassista."
                    )

                else:

                    valid = True

        # =====================================
        # SEGNALE NON RICONOSCIUTO
        # =====================================

        else:

            rejection_reason = (
                "Segnale non riconosciuto."
            )

        # =====================================
        # LOG
        # =====================================

        if valid:

            Logger.success(
                f"Segnale validato: {signal}"
            )

        else:

            Logger.info(
                f"Segnale rifiutato: "
                f"{rejection_reason}"
            )

        # =====================================
        # OUTPUT
        # =====================================

        return {

            "valid": valid,

            "signal": signal,

            "score": score,

            "confidence": confidence,

            "dominant_direction":
                dominant_direction,

            "conflict":
                conflict,

            "bullish_score":
                bullish_score,

            "bearish_score":
                bearish_score,

            "reasons":
                reasons,

            "warnings":
                warnings,

            "rejection_reason":
                rejection_reason

        }

    # =====================================
    # GENERAZIONE
    # =====================================

    def generate_signal(
        self,
        decision,
        brain,
        risk
    ):

        if not risk.get(
            "allow_trade",
            False
        ):

            return "HOLD"

        action = str(
            brain.get(
                "action",
                "HOLD"
            )
        ).upper()

        if action in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL",
            "HOLD"
        ):

            return action

        return "HOLD"

    # =====================================
    # BUY
    # =====================================

    def is_buy(
        self,
        signal
    ):

        return str(
            signal
        ).upper() in (
            "BUY",
            "STRONG BUY"
        )

    # =====================================
    # SELL
    # =====================================

    def is_sell(
        self,
        signal
    ):

        return str(
            signal
        ).upper() in (
            "SELL",
            "STRONG SELL"
        )

    # =====================================
    # HOLD
    # =====================================

    def is_hold(
        self,
        signal
    ):

        return str(
            signal
        ).upper() == "HOLD"

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        Logger.info(
            "Signal Manager resettato."
        )