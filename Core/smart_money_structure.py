from Logs.logger import Logger


class SmartMoneyStructure:

    def __init__(self):

        Logger.success(
            "Smart Money Structure V4 inizializzato."
        )

    # =====================================
    # SWING HIGH / SWING LOW
    # =====================================

    def _find_swings(self, data, strength=2):

        if len(data) < (strength * 2) + 1:

            return [], []

        highs = []
        lows = []

        for i in range(
            strength,
            len(data) - strength
        ):

            current_high = float(
                data["High"].iloc[i]
            )

            current_low = float(
                data["Low"].iloc[i]
            )

            left_highs = [
                float(data["High"].iloc[j])
                for j in range(
                    i - strength,
                    i
                )
            ]

            right_highs = [
                float(data["High"].iloc[j])
                for j in range(
                    i + 1,
                    i + strength + 1
                )
            ]

            left_lows = [
                float(data["Low"].iloc[j])
                for j in range(
                    i - strength,
                    i
                )
            ]

            right_lows = [
                float(data["Low"].iloc[j])
                for j in range(
                    i + 1,
                    i + strength + 1
                )
            ]

            if (
                current_high > max(left_highs)
                and current_high > max(right_highs)
            ):

                highs.append({
                    "index": i,
                    "price": current_high
                })

            if (
                current_low < min(left_lows)
                and current_low < min(right_lows)
            ):

                lows.append({
                    "index": i,
                    "price": current_low
                })

        return highs, lows

    # =====================================
    # BOS - BREAK OF STRUCTURE
    # =====================================

    def detect_bos(
        self,
        data,
        lookback=20
    ):

        if len(data) < 10:

            return {
                "bos_bullish": False,
                "bos_bearish": False
            }

        working_data = data.tail(
            lookback + 5
        )

        highs, lows = self._find_swings(
            working_data,
            strength=2
        )

        if not highs and not lows:

            return {
                "bos_bullish": False,
                "bos_bearish": False
            }

        last_close = float(
            working_data["Close"].iloc[-1]
        )

        bos_bullish = False
        bos_bearish = False

        # -------------------------------
        # ULTIMO SWING HIGH
        # -------------------------------

        if highs:

            last_swing_high = highs[-1]["price"]

            bos_bullish = (
                last_close > last_swing_high
            )

        # -------------------------------
        # ULTIMO SWING LOW
        # -------------------------------

        if lows:

            last_swing_low = lows[-1]["price"]

            bos_bearish = (
                last_close < last_swing_low
            )

        return {

            "bos_bullish": bos_bullish,

            "bos_bearish": bos_bearish

        }

    # =====================================
    # CHoCH - CHANGE OF CHARACTER
    # =====================================

    def detect_choch(
        self,
        data,
        lookback=20
    ):

        if len(data) < 10:

            return {
                "detected": False,
                "direction": None
            }

        working_data = data.tail(
            lookback + 5
        )

        highs, lows = self._find_swings(
            working_data,
            strength=2
        )

        if len(highs) < 2 or len(lows) < 2:

            return {
                "detected": False,
                "direction": None
            }

        last_close = float(
            working_data["Close"].iloc[-1]
        )

        # =================================
        # STRUTTURA PRECEDENTE
        # =================================

        previous_high = highs[-2]["price"]
        latest_high = highs[-1]["price"]

        previous_low = lows[-2]["price"]
        latest_low = lows[-1]["price"]

        # =================================
        # STRUTTURA RIBASSISTA
        # =================================

        bearish_structure = (
            latest_high < previous_high
            and latest_low < previous_low
        )

        # =================================
        # STRUTTURA RIALZISTA
        # =================================

        bullish_structure = (
            latest_high > previous_high
            and latest_low > previous_low
        )

        # =================================
        # CHoCH RIALZISTA
        # =================================
        #
        # Struttura precedente ribassista
        # + rottura dell'ultimo swing high.
        #

        if (
            bearish_structure
            and last_close > latest_high
        ):

            return {
                "detected": True,
                "direction": "BULLISH"
            }

        # =================================
        # CHoCH RIBASSISTA
        # =================================
        #
        # Struttura precedente rialzista
        # + rottura dell'ultimo swing low.
        #

        if (
            bullish_structure
            and last_close < latest_low
        ):

            return {
                "detected": True,
                "direction": "BEARISH"
            }

        return {
            "detected": False,
            "direction": None
        }