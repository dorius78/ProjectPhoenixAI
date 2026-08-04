"""
========================================
PROJECT PHOENIX AI
Database Manager
Versione 3.0
========================================
"""

import sqlite3

from Logs.logger import Logger


class DatabaseManager:

    def __init__(self):

        Logger.success(

            "Database Manager V3 inizializzato."

        )

        self.connection = sqlite3.connect(

            "phoenix_ai.db"

        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    # =====================================
    # CREA TABELLE
    # =====================================

    def create_tables(self):

        self.cursor.execute("""

        CREATE TABLE IF NOT EXISTS trades(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            symbol TEXT,

            side TEXT,

            entry REAL,

            exit REAL,

            stop_loss REAL,

            take_profit REAL,

            pnl REAL,

            status TEXT,

            reason TEXT,

            open_time TEXT,

            close_time TEXT,

            duration REAL,

            result TEXT,

            risk_reward REAL

        )

        """)

        self.connection.commit()

    # =====================================
    # SALVA TRADE
    # =====================================

    def save_trade(

        self,

        trade

    ):

        self.cursor.execute(

            """

            INSERT INTO trades(

                symbol,

                side,

                entry,

                exit,

                stop_loss,

                take_profit,

                pnl,

                status,

                reason,

                open_time,

                close_time,

                duration,

                result,

                risk_reward

            )

            VALUES(

                ?,?,?,?,?,?,?,?,?,?,?,?,?,?

            )

            """,

            (

                trade.get("symbol"),

                trade.get("side"),

                trade.get("entry"),

                trade.get("exit"),

                trade.get("stop_loss"),

                trade.get("take_profit"),

                trade.get("pnl"),

                trade.get("status"),

                trade.get("reason"),

                str(

                    trade.get("open_time")

                ),

                str(

                    trade.get("close_time")

                ),

                trade.get(

                    "duration",

                    0

                ),

                trade.get(

                    "result",

                    "UNKNOWN"

                ),

                trade.get(

                    "risk_reward",

                    0

                )

            )

        )

        self.connection.commit()

    # =====================================
    # TUTTI I TRADE
    # =====================================

    def load_trades(self):

        self.cursor.execute(

            "SELECT * FROM trades ORDER BY id DESC"

        )

        return self.cursor.fetchall()

    # =====================================
    # CONTA
    # =====================================

    def count(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades"

        )

        return self.cursor.fetchone()[0]

    # =====================================
    # WIN
    # =====================================

    def wins(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades WHERE pnl>0"

        )

        return self.cursor.fetchone()[0]

    # =====================================
    # LOSS
    # =====================================

    def losses(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades WHERE pnl<0"

        )

        return self.cursor.fetchone()[0]

    # =====================================
    # PROFITTO
    # =====================================

    def total_profit(self):

        self.cursor.execute(

            "SELECT SUM(pnl) FROM trades"

        )

        result = self.cursor.fetchone()[0]

        if result is None:

            return 0

        return round(result, 2)

    # =====================================
    # RESET
    # =====================================

    def reset(self):

        self.cursor.execute(

            "DELETE FROM trades"

        )

        self.connection.commit()

        Logger.warning(

            "Database azzerato."

        )

    # =====================================
    # CHIUSURA
    # =====================================

    def close(self):

        self.connection.close()