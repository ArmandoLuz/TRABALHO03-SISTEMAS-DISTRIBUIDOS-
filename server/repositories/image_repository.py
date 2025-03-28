from datetime import datetime
import sqlite3

from server.settings import settings


def image_repository(filename, filter_type, filepath):
    # Salvar no banco de dados
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(settings.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO images (filename, filter, timestamp, path) VALUES (?, ?, ?, ?)",
                   (filename, filter_type, timestamp, filepath))
    conn.commit()
    conn.close()