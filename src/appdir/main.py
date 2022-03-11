import os
import sys
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from libdir import mylog, mylib

mylog.config()
logging.info('%s', __name__)
