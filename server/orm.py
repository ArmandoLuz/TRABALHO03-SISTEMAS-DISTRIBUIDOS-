# Configuração do banco de dados
import sqlite3

from server.settings import settings


def init_db():
    conn = sqlite3.connect(settings.DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS images (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        filename TEXT,
                        filter TEXT,
                        timestamp TEXT,
                        path TEXT
                    )''')
    conn.commit()
    conn.close()