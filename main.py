import sys

from PyQt5.QtWidgets import QApplication

from client.view.main_window import run_client
from server.controller import app
import threading

from server.orm import init_db


def start_server():
    init_db()
    app.run(host="0.0.0.0", port=5000)

if __name__ == '__main__':
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    run_client()