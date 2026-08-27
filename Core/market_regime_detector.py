from Logs.logger import Logger


class MarketRegimeDetector:

    def __init__(self):
        Logger.success("Market Regime Detector V1 inizializzato.")

    def detect(self, indicators, analysis=None):

        atr = float(indicators.get("atr", 0.0) or 0.0)
        adx = float(indicators.get("adx", 0.0) or 0.0)

        upper = float(indicators.get("bollinger_upper", 0.0) or 0.0)
        lower = float(indicators.get("bollinger_lower", 0.0) or 0.0)
        price = float(
            indicators.get("price",
            indicators.get("close", 0.0)) or 0.0
        )

        if price <= 0:
            return {
                "regime": "UNKNOWN",
                "confidence": 0.0,
                "reason": "Prezzo non disponibile"
            }

        width = upper - lower if upper > lower else 0.0
        volatility_ratio = atr / price if price > 0 else 0.0

        if adx >= 25:
            regime = "TRENDING"
        elif width > 0 and volatility_ratio < 0.002:
            regime = "LOW_VOLATILITY"
        elif adx < 20:
            regime = "SIDEWAYS"
        else:
            regime = "TRANSITION"

        if regime == "TRENDING":
            confidence = min(1.0, adx / 50.0)
        elif regime == "SIDEWAYS":
            confidence = min(1.0, (25.0 - adx) / 25.0)
        else:
            confidence = 0.5

        return {
            "regime": regime,
            "confidence": round(confidence, 4),
            "adx": adx,
            "atr": atr,
            "volatility_ratio": round(volatility_ratio, 6),
            "bollinger_width": width
        }
