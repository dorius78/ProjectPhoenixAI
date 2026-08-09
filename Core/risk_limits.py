"""
========================================
PROJECT PHOENIX AI
Risk Limits
Versione 1.0
========================================
"""

from Logs.logger import Logger


class RiskLimits:

    def __init__(self):

        Logger.success(
            "Risk Limits V1 inizializzato."
        )

    def evaluate(self, analysis):

        # Prima cercava chiavi ("trend", "momentum", "rsi" come
        # stringa "RIALZISTA"/"NEUTRALE") che non esistono nel
        # dizionario di analisi reale (che usa trend_bullish/
        # trend_bearish booleani, adx_strong, rsi numerico): il
        # punteggio finiva sempre a 50 ("MEDIO"), qualunque fosse
        # la situazione di mercato vera.

        score = 50

        if analysis.get("trend_bullish") or analysis.get("trend_bearish"):

            score += 20

        if analysis.get("adx_strong"):

            score += 20

        rsi = float(analysis.get("rsi", 50))

        if 40 <= rsi <= 60:

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