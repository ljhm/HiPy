# -*- coding: utf-8 -*-

"""
Log to stdout and file with rotating.

    import logging
    import mylog

    mylog.config()
    logging.info('hello')
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler


def config():
    """ Call config() once in top-level to log. """

    filename = '../log/myapp.log'
    size = 10 * 1024 * 1024  # 10M
    count = 10
    level = logging.DEBUG
    fmt = "%(asctime)s %(levelname)s %(pathname)s:%(lineno)d:%(funcName)s: %(message)s"
    path = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(path, filename)
    file_handler = RotatingFileHandler(filename, maxBytes=size, backupCount=count)
    console_handler = logging.StreamHandler(sys.stdout)
    handlers = [file_handler, console_handler]
    logging.basicConfig(handlers=handlers, level=level, format=fmt)

    logging.info('log filename: %s', filename)
