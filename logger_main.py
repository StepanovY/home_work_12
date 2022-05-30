import logging


def creat_logger():
    logger = logging.getLogger('logger')
    logger.setLevel('DEBUG')

    console_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('logs/logger_main.log', encoding="utf-8")
    formatter = logging.Formatter(fmt='%(asctime)s : %(message)s')

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
