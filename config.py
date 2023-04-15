import os
from dotenv import load_dotenv

load_dotenv()

SOURCE_FILE_PATH = os.environ.get('SOURCE_FILE_PATH', './Pulse.txt')
