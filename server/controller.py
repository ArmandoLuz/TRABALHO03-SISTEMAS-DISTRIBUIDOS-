from flask import Flask, request, jsonify, send_file
import os
import sqlite3
from server.settings import settings

from server.processing.image_process import processing_image, get_filters

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_image():
    if "image" not in request.files or "filter" not in request.form:
        return jsonify({"error": "Envie uma imagem e escolha um filtro."}), 400

    file = request.files["image"]
    filter_type = request.form["filter"]
    if filter_type not in list(get_filters().keys()):
        return jsonify({"error": "Filtro inválido."}), 400

    processed_filepath = processing_image(file, filter_type)

    return send_file(processed_filepath, mimetype='image/png')

@app.route("/list_images")
def list_images():
    conn = sqlite3.connect(settings.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images")
    images = cursor.fetchall()
    conn.close()
    return images

@app.route("/image/<image_id>")
def get_image(image_id):
    conn = sqlite3.connect(settings.DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM images WHERE id=?", (image_id,))
    image = cursor.fetchone()
    conn.close()
    return send_file(image[4], mimetype='image/png')

