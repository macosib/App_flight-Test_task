import logging

log_format = f"%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"

def get_info_handler():
    """
    Add handler
    """
    info_handler = logging.StreamHandler()
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(logging.Formatter(log_format))
    return info_handler

def get_logger(name):
    """
    Create logger. For name using __name__.
    :param name: str
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_info_handler())
    return logger