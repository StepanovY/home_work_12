import json
from json import JSONDecodeError

from classes.exception import DataError, FileTypeError


def get_loud_posts():
    """Загрузка списка постов из файла"""
    try:
        with open("posts.json", 'r', encoding='utf-8') as file:
            loud_posts = json.load(file)
    except (FileNotFoundError, JSONDecodeError):
        raise DataError('Файл поврежден')
    return loud_posts


def uploads_post(picture, content):
    """Добавление поста в список постов"""
    data = {'pic': picture, 'content': content}
    loud_posts = get_loud_posts()
    loud_posts.append(data)
    with open("posts.json", 'w', encoding='utf-8') as file:
        return json.dump(loud_posts, file, ensure_ascii=False, indent=2)


def search_posts(content):
    """
    Поиск постов по содержимому
    """
    content_lower = content.lower()
    post_found = []
    posts = get_loud_posts()
    for post in posts:
        if content_lower in post['content'].lower():
            post_found.append(post)
    return post_found
