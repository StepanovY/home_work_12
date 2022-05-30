import logging

from flask import Blueprint, request, render_template

import functions
from classes.exception import FileTypeError

loader_blueprint = Blueprint('loader_blueprint', __name__, template_folder='templates')

logger = logging.getLogger('logger')


def is_filetype_is_valid(file_type):
    if file_type.lower() not in ['jpg', 'bmp', 'png', 'gif', 'tiff']:
        logger.info('загруженный файл - не картинка')
        return False
    return True

@loader_blueprint.route('/post_form/')
def upload_index():
    return render_template('post_form.html')


@loader_blueprint.route('/post_uploaded/', methods=["POST"])
def upload_posts():
    picture = request.files.get('picture')
    contents = request.form.get('content')
    filename = picture.filename
    file_type = filename.split('.')[-1]
    if file_type.lower() not in ['jpg', 'png', 'gif', 'tiff']:
        raise FileTypeError('Не поддерживаемый формат')
    picture.save(f'./uploads/images/{filename}')
    file = f'/uploads/images/{filename}'
    functions.uploads_post(file, contents)
    return render_template('post_uploaded.html', filename=picture, contents=contents)

@loader_blueprint.errorhandler(FileTypeError)
def file_error(e):
    logger.error("Не поддерживаемый формат")
    return "Не поддерживаемый формат"