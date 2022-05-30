import logging
from flask import Flask, request, render_template, send_from_directory

from loader.views import loader_blueprint
from main.views import main_blueprint
import logger_main

UPLOAD_FOLDER = "uploads/images"


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.config['JSON_AS_ASCII'] = False

logger_main.creat_logger()
logger = logging.getLogger('logger')

@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
