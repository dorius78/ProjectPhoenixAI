import yfinance as yf


class YFinanceProvider:

    def __init__(self):
        print("Yahoo Finance Provider inizializzato.")

    # =====================================
    # PREZZO CORRENTE
    # =====================================

    def get_price(self, symbol):

        try:

            ticker = yf.Ticker(symbol)

            data = ticker.history(
                period="5d",
                interval="1d",
                auto_adjust=False
            )

            if data is not None and not data.empty:

                close = data["Close"].dropna()

                if not close.empty:

                    price = float(close.iloc[-1])

                    print(
                        f"{symbol} -> {price}"
                    )

                    return price

            # Tentativo alternativo
            try:

                fast_info = ticker.fast_info

                if fast_info is not None:

                    price = fast_info.get(
                        "lastPrice"
                    )

                    if price is not None:

                        price = float(price)

                        print(
                            f"{symbol} -> {price}"
                        )

                        return price

            except Exception:
                pass

            print(
                f"Nessun prezzo trovato per {symbol}"
            )

            return None

        except Exception as e:

            print(
                f"Errore Yahoo Finance "
                f"prezzo {symbol}: {e}"
            )

            return None

    # =====================================
    # DATI STORICI
    # =====================================

    def get_historical_data(
        self,
        symbol,
        period="3mo",
        interval="1h"
    ):

        try:

            print(
                f"Download dati {symbol} "
                f"({period} - {interval})"
            )

            ticker = yf.Ticker(symbol)

            data = ticker.history(
                period=period,
                interval=interval,
                auto_adjust=False,
                actions=False
            )

            if data is None or data.empty:

                print(
                    f"Nessun dato storico "
                    f"ricevuto per {symbol}"
                )

                return None

            # Normalizzazione colonne
            data = data.copy()

            data.columns = [
                str(column)
                for column in data.columns
            ]

            # Manteniamo solamente le colonne
            # necessarie al motore di trading.
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
                    "Colonne mancanti: "
                    f"{missing}"
                )

                return None

            data = data[
                required_columns
            ].copy()

            # Elimina righe senza prezzi
            data = data.dropna(
                subset=[
                    "Open",
                    "High",
                    "Low",
                    "Close"
                ]
            )

            if data.empty:

                print(
                    f"Dati inutilizzabili "
                    f"per {symbol}"
                )

                return None

            # Volume può essere assente/null
            # in alcuni strumenti.
            data["Volume"] = (
                data["Volume"]
                .fillna(0)
            )

            # Conversione numerica
            for column in required_columns:

                data[column] = (
                    data[column]
                    .astype(float)
                )

            print(
                f"Dati ricevuti: "
                f"{len(data)} candele"
            )

            print(
                f"Periodo: "
                f"{data.index[0]} -> "
                f"{data.index[-1]}"
            )

            return data

        except Exception as e:

            print(
                f"Errore Yahoo Finance "
                f"storico {symbol}: {e}"
            )

            return None