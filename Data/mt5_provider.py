import MetaTrader5 as mt5
import pandas as pd

from Config.mt5_credentials import SYMBOL_MAP


class MT5Provider:

    def __init__(self):
        self.initialized = False

    # =====================================
    # CONNESSIONE
    # =====================================

    def connect(self):

        if self.initialized:
            return True

        ok = mt5.initialize()

        if not ok:
            print(
                f"Errore inizializzazione MT5: "
                f"{mt5.last_error()}"
            )
            return False

        self.initialized = True

        return True

    # =====================================
    # DISCONNESSIONE
    # =====================================

    def disconnect(self):

        if self.initialized:
            mt5.shutdown()
            self.initialized = False

    # =====================================
    # MAPPATURA SIMBOLO
    # =====================================

    def _map_symbol(self, symbol):

        return SYMBOL_MAP.get(
            symbol,
            symbol
        )

    # =====================================
    # PREZZO CORRENTE
    # =====================================

    def get_price(self, symbol):

        if not self.connect():
            return None

        mt5_symbol = self._map_symbol(symbol)

        info = mt5.symbol_info_tick(
            mt5_symbol
        )

        if info is None:

            print(
                f"Nessun tick MT5 per "
                f"{mt5_symbol}"
            )

            return None

        # Per un prezzo unico utilizziamo
        # il midpoint Bid/Ask quando entrambi
        # sono disponibili.

        bid = float(info.bid)
        ask = float(info.ask)

        if bid > 0 and ask > 0:

            price = (bid + ask) / 2.0

        elif bid > 0:

            price = bid

        elif ask > 0:

            price = ask

        else:

            return None

        return float(price)

    # =====================================
    # DATI STORICI
    # =====================================

    def get_historical_data(
        self,
        symbol,
        period="3mo",
        interval="1h"
    ):

        if not self.connect():
            return None

        mt5_symbol = self._map_symbol(symbol)

        timeframe_map = {

            "1m": mt5.TIMEFRAME_M1,
            "5m": mt5.TIMEFRAME_M5,
            "15m": mt5.TIMEFRAME_M15,
            "30m": mt5.TIMEFRAME_M30,
            "1h": mt5.TIMEFRAME_H1,
            "4h": mt5.TIMEFRAME_H4,
            "1d": mt5.TIMEFRAME_D1

        }

        timeframe = timeframe_map.get(
            interval
        )

        if timeframe is None:

            print(
                f"Intervallo MT5 non supportato: "
                f"{interval}"
            )

            return None

        rates = mt5.copy_rates_from_pos(
            mt5_symbol,
            timeframe,
            0,
            self._period_to_bars(
                period,
                interval
            )
        )

        if rates is None or len(rates) == 0:

            print(
                f"Nessun dato storico MT5 "
                f"per {mt5_symbol}"
            )

            return None

        data = pd.DataFrame(rates)

        data["time"] = pd.to_datetime(
            data["time"],
            unit="s",
            utc=True
        )

        data = data.set_index("time")

        data = data.rename(
            columns={
                "open": "Open",
                "high": "High",
                "low": "Low",
                "close": "Close",
                "tick_volume": "Volume"
            }
        )

        required_columns = [
            "Open",
            "High",
            "Low",
            "Close",
            "Volume"
        ]

        missing = [
            column
            for column in required_columns
            if column not in data.columns
        ]

        if missing:

            print(
                f"Colonne MT5 mancanti: "
                f"{missing}"
            )

            return None

        data = data[
            required_columns
        ].copy()

        data = data.dropna(
            subset=[
                "Open",
                "High",
                "Low",
                "Close"
            ]
        )

        if data.empty:
            return None

        for column in required_columns:

            data[column] = (
                data[column]
                .astype(float)
            )

        return data

    # =====================================
    # CONVERSIONE PERIODO → NUMERO CANDELE
    # =====================================

    def _period_to_bars(
        self,
        period,
        interval
    ):

        period_days = {

            "1d": 1,
            "5d": 5,
            "1mo": 30,
            "3mo": 90,
            "6mo": 180,
            "1y": 365

        }.get(
            period,
            90
        )

        minutes_map = {

            "1m": 1,
            "5m": 5,
            "15m": 15,
            "30m": 30,
            "1h": 60,
            "4h": 240,
            "1d": 1440

        }

        minutes = minutes_map.get(
            interval,
            60
        )

        bars = int(
            (period_days * 1440)
            / minutes
        )

        # Limite prudenziale per il primo test.

        return max(
            10,
            min(
                bars,
                5000
            )
        )
