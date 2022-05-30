import logging

from flask import Blueprint, request, render_template

import functions
from classes.exception import DataError

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

logger = logging.getLogger('logger')


@main_blueprint.route('/')
def main_index():
    return render_template('index.html')


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get('s', '')
    posts = functions.search_posts(s)
    logger.info(f'Выполняется поиск {s}')
    return render_template('post_list.html', posts=posts, s=s)


@main_blueprint.errorhandler(DataError)
def data_error(e):
    logger.error("Файл с данными поврежден")
    return "Файл с данными поврежден"