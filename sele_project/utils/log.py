import logging

class Log():
    def __init__(self):
        logging.basicConfig(
            level = logging.INFO,
            format = '%(asctime)s %(levelname)s %(message)s',
            datefmt = '%Y-%m-%d-%H-%M-%S',
            filemode = 'w'
        )
    def add_log(self):
        out_str = page + ':' + func + ':' + des

