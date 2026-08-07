"""
========================================
PROJECT PHOENIX AI
Phoenix Brain Logic
Versione 2.0
========================================
"""

from Logs.logger import Logger


class PhoenixBrainLogic:

    def __init__(self):

        Logger.success(
            "Phoenix Brain Logic V2 inizializzato."
        )

    def calculate(self, analysis, risk):

        score = 50

        reasons = []
        warnings = []

        # =====================================
        # TREND
        # =====================================

        if analysis.get("trend_bullish"):
            score += 20
            reasons.append("Trend rialzista")
        elif analysis.get("trend_bearish"):
            score -= 20
            warnings.append("Trend ribassista")

        # =====================================
        # EMA
        # =====================================
        # Prima "ema_alignment" dava sempre lo stesso bonus rialzista
        # indipendentemente dalla direzione. Ora e' simmetrico.

        if analysis.get("ema_alignment_bullish"):
            score += 10
            reasons.append("EMA allineate al rialzo")
        elif analysis.get("ema_alignment_bearish"):
            score -= 10
            warnings.append("EMA allineate al ribasso")

        # =====================================
        # MACD
        # =====================================

        if analysis.get("macd_buy"):
            score += 10
            reasons.append("MACD BUY")
        elif analysis.get("macd_sell"):
            score -= 10
            warnings.append("MACD SELL")

        # =====================================
        # RSI
        # =====================================

        rsi = float(analysis.get("rsi", 50))

        if rsi < 30:
            score += 15
            reasons.append("RSI ipervenduto")
        elif rsi > 70:
            score -= 15
            warnings.append("RSI ipercomprato")

        # La fascia centrale del RSI (45-60) prima dava sempre un
        # bonus rialzista fisso. E' un valore neutro per definizione,
        # quindi ora non influenza piu' il punteggio in nessuna
        # direzione.

        # =====================================
        # ADX (forza del trend)
        # =====================================
        # ADX misura solo QUANTO e' forte il trend, non la direzione.
        # Prima dava sempre un bonus rialzista fisso: ora amplifica
        # la direzione gia' indicata dal trend, in entrambi i sensi.

        if analysis.get("adx_strong"):

            if analysis.get("trend_bullish"):
                score += 10
                reasons.append("Trend forte (rialzista)")
            elif analysis.get("trend_bearish"):
                score -= 10
                warnings.append("Trend forte (ribassista)")

        # =====================================
        # VOLUME
        # =====================================
        # Stesso principio dell'ADX: il volume da solo non ha
        # direzione, conferma quella del trend in corso.

        if analysis.get("volume_high"):

            if analysis.get("trend_bullish"):
                score += 10
                reasons.append("Volume elevato (conferma rialzo)")
            elif analysis.get("trend_bearish"):
                score -= 10
                warnings.append("Volume elevato (conferma ribasso)")

        # =====================================
        # SMART MONEY - STRUTTURA (BOS)
        # =====================================

        if analysis.get("bos_bullish"):
            score += 15
            reasons.append("BOS Rialzista")

        if analysis.get("bos_bearish"):
            score -= 15
            warnings.append("BOS Ribassista")

        # =====================================
        # SMART MONEY - CHoCH
        # =====================================
        # Prima un CHoCH rialzista o ribassista davano lo stesso
        # bonus fisso rialzista. Ora sono distinti.

        if analysis.get("choch_bullish"):
            score += 10
            reasons.append("CHoCH Rialzista")
        elif analysis.get("choch_bearish"):
            score -= 10
            warnings.append("CHoCH Ribassista")

        # =====================================
        # SMART MONEY - FAIR VALUE GAP
        # =====================================

        if analysis.get("fvg_bullish"):
            score += 8
            reasons.append("Fair Value Gap Rialzista")
        elif analysis.get("fvg_bearish"):
            score -= 8
            warnings.append("Fair Value Gap Ribassista")

        # =====================================
        # SMART MONEY - ORDER BLOCK
        # =====================================

        if analysis.get("order_block_bullish"):
            score += 10
            reasons.append("Order Block Rialzista")
        elif analysis.get("order_block_bearish"):
            score -= 10
            warnings.append("Order Block Ribassista")

        # =====================================
        # SMART MONEY - LIQUIDITY SWEEP
        # =====================================

        if analysis.get("liquidity_bullish"):
            score += 8
            reasons.append("Liquidity Sweep Rialzista")
        elif analysis.get("liquidity_bearish"):
            score -= 8
            warnings.append("Liquidity Sweep Ribassista")

        score = max(0, min(score, 100))

        # La confidence prima era identica allo score: per un SELL
        # forte (score basso, es. 20) risultava una confidence bassa,
        # mentre per un BUY forte (score alto, es. 80) risultava alta.
        # Il Signal Manager valida i segnali semplici (non STRONG) solo
        # sopra una soglia di confidence: cosi' i SELL non l'avrebbero
        # praticamente mai superata. Ora la confidence misura la
        # distanza dal punto neutro (50), in modo simmetrico per
        # entrambe le direzioni.
        confidence = abs(score - 50) * 2
        confidence = max(0, min(confidence, 100))

        if risk["risk_level"] == "MEDIO":
            confidence -= 10
        elif risk["risk_level"] == "ALTO":
            confidence -= 20

        confidence = max(0, min(confidence, 100))

        return {
            "score": score,
            "confidence": confidence,
            "reasons": reasons,
            "warnings": warnings
        }