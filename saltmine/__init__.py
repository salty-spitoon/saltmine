import logging

logging.captureWarnings(True)
formatter = logging.Formatter('[%(asctime)s %(levelname)s] [%(name)s.%(funcName)s] %(message)s')
handler = logging.FileHandler('debug.log')
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)
