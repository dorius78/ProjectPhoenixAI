from Core.analysis_engine import AnalysisEngine
from Core.paper_trading_engine import PaperTradingEngine
from Data.mt5_provider import MT5Provider
from Config.settings import SYMBOL


class PaperDecisionBridge:

    def __init__(self):

        self.provider = MT5Provider()
        self.analysis_engine = AnalysisEngine()

        self.paper_engine = PaperTradingEngine()

    # =====================================
    # SINGOLA ITERAZIONE
    # =====================================

    def run_once(
        self,
        symbol=SYMBOL,
        period="5d",
        interval="1h"
    ):

        print()
        print("=" * 90)
        print("PHOENIX AI - PAPER DECISION BRIDGE")
        print("=" * 90)

        # =================================
        # 1. MT5
        # =================================

        if not self.provider.connect():

            return {
                "status": "ERROR",
                "reason": "MT5 connection failed"
            }

        # =================================
        # 2. DATI STORICI
        # =================================

        data = self.provider.get_historical_data(
            symbol=symbol,
            period=period,
            interval=interval
        )

        if data is None or data.empty:

            self.provider.disconnect()

            return {
                "status": "ERROR",
                "reason": "No market data"
            }

        # =================================
        # 3. ESCLUDI CANDLE CORRENTE
        # =================================

        if len(data) < 20:

            self.provider.disconnect()

            return {
                "status": "ERROR",
                "reason": "Insufficient candles"
            }

        closed_data = data.iloc[:-1].copy()

        if closed_data.empty:

            self.provider.disconnect()

            return {
                "status": "ERROR",
                "reason": "No closed candle"
            }

        price = float(
            closed_data["Close"].iloc[-1]
        )

        print()
        print("[MT5]")
        print("SYMBOL =", symbol)
        print("CLOSED CANDLE =", closed_data.index[-1])
        print("PRICE =", price)

        # =================================
        # 4. PAPER ACCOUNT
        # =================================

        account_balance = (
            self.paper_engine.get_balance()
        )

        print()
        print("[PAPER ACCOUNT]")
        print("BALANCE =", account_balance)

        # =================================
        # 5. PHOENIX ANALYSIS
        # =================================

        result = self.analysis_engine.analyze(

            data=closed_data,

            price=price,

            symbol=symbol,

            account_balance=account_balance

        )

        if not isinstance(result, dict):

            self.provider.disconnect()

            return {
                "status": "ERROR",
                "reason": "Analysis returned invalid result"
            }

        analysis = result.get(
            "analysis",
            {}
        )

        decision = result.get(
            "decision",
            {}
        )

        risk = result.get(
            "risk",
            {}
        )

        signal = result.get(
            "signal",
            {}
        )

        # =================================
        # 6. OUTPUT DECISION
        # =================================

        action = decision.get(
            "action"
        )

        confidence = decision.get(
            "confidence"
        )

        signal_valid = signal.get(
            "valid",
            False
        )

        allow_trade = risk.get(
            "allow_trade",
            False
        )

        atr = analysis.get(
            "atr"
        )

        print()
        print("[PHOENIX DECISION]")
        print("ACTION       =", action)
        print("CONFIDENCE   =", confidence)
        print("RISK LEVEL   =", risk.get("risk_level"))
        print("RISK SCORE   =", risk.get("risk_score"))
        print("ALLOW TRADE  =", allow_trade)
        print("SIGNAL       =", signal.get("signal"))
        print("SIGNAL VALID =", signal_valid)
        print("ATR          =", atr)

        # =================================
        # 7. SAFETY GATE
        # =================================

        if not signal_valid:

            self.provider.disconnect()

            print()
            print("[PAPER]")
            print("WAIT - SIGNAL NON VALIDO")
            print("NESSUNA POSIZIONE APERTA")

            return {
                "status": "WAIT",
                "reason": signal.get(
                    "rejection_reason",
                    "Signal invalid"
                ),
                "analysis": analysis,
                "decision": decision,
                "risk": risk,
                "signal": signal,
                "trade": None,
                "position": None
            }

        if not allow_trade:

            self.provider.disconnect()

            print()
            print("[PAPER]")
            print("WAIT - RISK GATE")
            print("NESSUNA POSIZIONE APERTA")

            return {
                "status": "WAIT",
                "reason": "Risk gate blocked trade",
                "analysis": analysis,
                "decision": decision,
                "risk": risk,
                "signal": signal,
                "trade": None,
                "position": None
            }

        if action not in (
            "BUY",
            "SELL",
            "STRONG BUY",
            "STRONG SELL"
        ):

            self.provider.disconnect()

            print()
            print("[PAPER]")
            print("WAIT - ACTION NON OPERATIVA")

            return {
                "status": "WAIT",
                "reason": "Action not tradable",
                "analysis": analysis,
                "decision": decision,
                "risk": risk,
                "signal": signal,
                "trade": None,
                "position": None
            }

        if atr is None or float(atr) <= 0:

            self.provider.disconnect()

            return {
                "status": "WAIT",
                "reason": "Invalid ATR",
                "analysis": analysis,
                "decision": decision,
                "risk": risk,
                "signal": signal,
                "trade": None,
                "position": None
            }

        # =================================
        # 8. TRADE MANAGER
        # =================================

        trade = self.analysis_engine.trade_manager.generate_trade(

            symbol=symbol,

            price=price,

            signal=action,

            atr=float(atr),

            account_balance=account_balance

        )

        if trade is None:

            self.provider.disconnect()

            print()
            print("[PAPER]")
            print("WAIT - TRADE BUILDER / RISK MANAGER")

            return {
                "status": "WAIT",
                "reason": "Trade rejected by TradeManager",
                "analysis": analysis,
                "decision": decision,
                "risk": risk,
                "signal": signal,
                "trade": None,
                "position": None
            }

        # =================================
        # 9. PAPER POSITION
        # =================================

        position = None

        if not self.paper_engine.has_position():

            position = self.paper_engine.open_trade(

                side=trade["side"],

                entry=trade["entry"],

                stop_loss=trade["stop_loss"],

                take_profit=trade["take_profit"],

                symbol=trade["symbol"],

                size=trade["size"]

            )

        self.provider.disconnect()

        # =================================
        # 10. RISULTATO
        # =================================

        print()
        print("[PAPER TRADE]")

        if position is None:

            print("NESSUNA NUOVA POSIZIONE")

            status = "NO_TRADE"

        else:

            print("POSIZIONE APERTA")
            print("SIDE       =", position["side"])
            print("ENTRY      =", position["entry"])
            print("STOP LOSS  =", position["stop_loss"])
            print("TAKE PROFIT =", position["take_profit"])
            print("SIZE       =", position["size"])

            status = "TRADE_OPENED"

        print()
        print("=" * 90)
        print("PAPER DECISION BRIDGE COMPLETATO")
        print("=" * 90)
        print("NESSUN ORDER_SEND")
        print("NESSUN ORDINE MT5")
        print("NESSUN TRADING LIVE")
        print("=" * 90)

        return {
            "status": status,
            "analysis": analysis,
            "decision": decision,
            "risk": risk,
            "signal": signal,
            "trade": trade,
            "position": position
        }

