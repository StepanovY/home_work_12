class DataError(Exception):
    """Файл поврежден"""
    pass


class FileTypeError(Exception):
    """Не поддерживаемый формат"""
    pass