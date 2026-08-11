"""
========================================
PROJECT PHOENIX AI
Database Manager
Versione 6.0
========================================
"""

import sqlite3

from Logs.logger import Logger


class DatabaseManager:

    def __init__(self, database_path="phoenix_ai.db"):

        Logger.success("Database Manager V6 inizializzato.")

        self.database_path = database_path

        self.connection = sqlite3.connect(
            self.database_path
        )

        self.cursor = self.connection.cursor()

        self.create_tables()

    # =====================================
    # CREA TABELLA
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
    # SALVA
    # =====================================

    def save_trade(self, trade):

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

                trade["symbol"],
                trade["side"],
                trade["entry"],
                trade["exit"],
                trade["stop_loss"],
                trade["take_profit"],
                trade["pnl"],
                trade["status"],
                trade["reason"],
                str(trade["open_time"]),
                str(trade["close_time"]),
                trade["duration"],
                trade["result"],
                trade["risk_reward"]

            )

        )

        self.connection.commit()

    # =====================================
    # ELENCO
    # =====================================

    def load_trades(self):

        self.cursor.execute(

            "SELECT * FROM trades ORDER BY id DESC"

        )

        return self.cursor.fetchall()

    # =====================================
    # STATISTICHE
    # =====================================

    def count(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades"

        )

        return self.cursor.fetchone()[0]

    def wins(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades WHERE pnl>0"

        )

        return self.cursor.fetchone()[0]

    def losses(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades WHERE pnl<0"

        )

        return self.cursor.fetchone()[0]

    def breakeven(self):

        self.cursor.execute(

            "SELECT COUNT(*) FROM trades WHERE pnl=0"

        )

        return self.cursor.fetchone()[0]

    def total_profit(self):

        self.cursor.execute(

            "SELECT SUM(pnl) FROM trades"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(value, 2)

    def gross_profit(self):

        self.cursor.execute(

            "SELECT SUM(pnl) FROM trades WHERE pnl>0"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(value, 2)

    def gross_loss(self):

        self.cursor.execute(

            "SELECT SUM(pnl) FROM trades WHERE pnl<0"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(abs(value), 2)

    def best_trade(self):

        self.cursor.execute(

            "SELECT MAX(pnl) FROM trades"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(value, 2)

    def worst_trade(self):

        self.cursor.execute(

            "SELECT MIN(pnl) FROM trades"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(value, 2)

    def average_profit(self):

        self.cursor.execute(

            "SELECT AVG(pnl) FROM trades"

        )

        value = self.cursor.fetchone()[0]

        return 0 if value is None else round(value, 2)

    def profit_factor(self):

        gp = self.gross_profit()

        gl = self.gross_loss()

        if gl == 0:

            return 0

        return round(gp / gl, 2)

    def win_rate(self):

        total = self.wins() + self.losses()

        if total == 0:

            return 0

        return round(

            self.wins() * 100 / total,

            2

        )

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
    # CLOSE
    # =====================================

    def close(self):

        self.connection.close()