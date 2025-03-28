from dotenv import load_dotenv

load_dotenv(".env")
import os

class Settings:
    def __init__(self, data):
        for key, value in data.items():
            setattr(self, key, value)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
data_settings = {
    "BASE_DIR": BASE_DIR,
    "UPLOAD_PATH": os.path.join(BASE_DIR, os.getenv("UPLOAD_PATH")),
    "DB_FILE": os.path.join(BASE_DIR, os.getenv("DB_PATH"), "database.db"),
    "DB_PATH": os.path.join(BASE_DIR, os.getenv("DB_PATH")),
    "PROCESSED_PATH": os.path.join(BASE_DIR, os.getenv("PROCESSED_PATH"))
}

settings = Settings(data_settings)


os.makedirs(settings.UPLOAD_PATH, exist_ok=True)
print(settings.UPLOAD_PATH)
os.makedirs(settings.PROCESSED_PATH, exist_ok=True)
os.makedirs(settings.DB_PATH, exist_ok=True)