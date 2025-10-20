import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# FIX 1: Define the directory path first
logs_dir = os.path.join(os.getcwd(), "logs")
# Now create the directory
os.makedirs(logs_dir, exist_ok=True)

# FIX 2: Create the full file path by joining the directory and filename
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,  # <-- FIX 3: Corrected 'lavel' to 'level'
)

