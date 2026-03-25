import logging
import os

LOG_DIR = os.path.join(os.getcwd(), "artifacts")
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(filename=os.path.join(LOG_DIR,"core.log"),
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(msg):
    logging.info(msg)

def log_error(msg):
    logging.error(msg)
