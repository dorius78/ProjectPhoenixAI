from pathlib import Path

path = Path(
    "Database/database_manager.py"
)

text = path.read_text(
    encoding="utf-8"
)

marker = '''    # =====================================
    # ELENCO
    # =====================================
'''

method = '''    # =====================================
    # VERIFICA TRADE ESISTENTE
    # =====================================

    def has_trade(self, trade_id):

        if trade_id is None:

            return False

        self.cursor.execute(

            """
            SELECT 1
            FROM trades
            WHERE trade_id = ?
            LIMIT 1
            """,

            (
                str(trade_id),
            )

        )

        return (
            self.cursor.fetchone()
            is not None
        )

'''

if marker not in text:
    raise RuntimeError(
        "STOP: marker DatabaseManager ELENCO non trovato"
    )

if "def has_trade(" in text:
    raise RuntimeError(
        "STOP: has_trade() esiste gia"
    )

text = text.replace(
    marker,
    method + marker,
    1
)

path.write_text(
    text,
    encoding="utf-8"
)

print("=" * 100)
print("E.27.12.77 DATABASE PATCH APPLICATA")
print("=" * 100)
print("BACKUP: OK")
print("has_trade(): AGGIUNTO")
print("Production database: MODIFICATO")
print("NESSUN ordine MT5")
print("NESSUNA apertura")
print("NESSUNA chiusura")
print("=" * 100)

