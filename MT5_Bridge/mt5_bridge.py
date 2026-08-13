"""
PROJECT PHOENIX AI
MT5 DATA BRIDGE v1.0

Collega il motore Python a MetaTrader 5 in sola lettura.
NON invia ordini.
"""

from __future__ import annotations

from typing import Any


class MT5DataBridge:
    def __init__(self, symbol: str = "EURUSD", timeframe: str = "M5"):
        self.symbol = symbol
        self.timeframe_name = timeframe.upper()
        self.mt5 = None
        self.connected = False

    def connect(self) -> bool:
        import MetaTrader5 as mt5

        self.mt5 = mt5
        if not mt5.initialize():
            self.connected = False
            return False

        if not mt5.symbol_select(self.symbol, True):
            self.disconnect()
            return False

        self.connected = True
        return True

    def disconnect(self) -> None:
        if self.mt5 is not None and self.connected:
            self.mt5.shutdown()
        self.connected = False

    def _timeframe(self):
        mapping = {
            "M1": self.mt5.TIMEFRAME_M1,
            "M5": self.mt5.TIMEFRAME_M5,
            "M15": self.mt5.TIMEFRAME_M15,
            "M30": self.mt5.TIMEFRAME_M30,
            "H1": self.mt5.TIMEFRAME_H1,
            "H4": self.mt5.TIMEFRAME_H4,
            "D1": self.mt5.TIMEFRAME_D1,
        }
        return mapping.get(self.timeframe_name, self.mt5.TIMEFRAME_M5)

    def tick(self) -> dict[str, Any]:
        if not self.connected:
            raise RuntimeError("MT5 non connesso.")

        tick = self.mt5.symbol_info_tick(self.symbol)
        if tick is None:
            raise RuntimeError(f"Nessun tick disponibile per {self.symbol}.")

        return {
            "symbol": self.symbol,
            "bid": float(tick.bid),
            "ask": float(tick.ask),
            "last": float(tick.last),
            "time": int(tick.time),
        }

    def candles(self, count: int = 200) -> list[dict[str, Any]]:
        if not self.connected:
            raise RuntimeError("MT5 non connesso.")

        rates = self.mt5.copy_rates_from_pos(
            self.symbol, self._timeframe(), 0, int(count)
        )

        if rates is None:
            raise RuntimeError(f"Candele non disponibili: {self.mt5.last_error()}")

        return [
            {
                "time": int(row["time"]),
                "Open": float(row["open"]),
                "High": float(row["high"]),
                "Low": float(row["low"]),
                "Close": float(row["close"]),
                "Volume": int(row["tick_volume"]),
            }
            for row in rates
        ]

    def snapshot(self, count: int = 200) -> dict[str, Any]:
        return {
            "source": "MetaTrader5",
            "symbol": self.symbol,
            "timeframe": self.timeframe_name,
            "tick": self.tick(),
            "candles": self.candles(count),
            "execution_enabled": False,
        }
