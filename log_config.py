import logging

logger = logging.getLogger("url-shortener")
file_handler = logging.FileHandler("app.log", mode="a")
stream_handler = logging.StreamHandler()


formatter = logging.Formatter(fmt='{asctime} - {levelname} - {message}', style='{', datefmt='%Y-%m-%d %H:%M')
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)