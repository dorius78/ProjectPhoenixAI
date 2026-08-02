"""
========================================
PROJECT PHOENIX AI
Risk Manager
Versione 7.1
========================================
"""

from Logs.logger import Logger


class RiskManager:

    def __init__(self):

        Logger.success("Risk Manager V7 inizializzato.")

        self.risk_reward_ratio = 2.0

    # =====================================
    # VALUTAZIONE RISCHIO
    # =====================================

    def evaluate(self, analysis):

        trend = analysis.get("trend", "NEUTRO")
        momentum = analysis.get("momentum", "NEUTRO")
        rsi = analysis.get("rsi", "NEUTRALE")

        score = 50

        if trend == "RIALZISTA":
            score += 20
        elif trend == "RIBASSISTA":
            score += 20

        if momentum in ["RIALZISTA", "RIBASSISTA"]:
            score += 20

        if rsi == "NEUTRALE":
            score += 10

        if score >= 70:
            level = "BASSO"
            allow_trade = True

        elif score >= 50:
            level = "MEDIO"
            allow_trade = True

        else:
            level = "ALTO"
            allow_trade = False

        return {
            "risk_level": level,
            "risk_score": score,
            "allow_trade": allow_trade
        }

    # =====================================
    # COSTRUZIONE TRADE
    # =====================================

    def build_trade(
        self,
        symbol,
        signal,
        current_price,
        atr
    ):

        signal = signal.upper()

        if signal not in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL"
        ):
            return None

        atr = float(atr)
        entry = float(current_price)

        rr = self.risk_reward_ratio

        if "BUY" in signal:

            stop_loss = entry - atr
            take_profit = entry + (atr * rr)
            side = "BUY"

        else:

            stop_loss = entry + atr
            take_profit = entry - (atr * rr)
            side = "SELL"

        return {

            "symbol": symbol,
            "side": side,
            "entry": round(entry, 6),
            "stop_loss": round(stop_loss, 6),
            "take_profit": round(take_profit, 6),
            "atr": round(atr, 6),
            "risk_reward": rr

        }