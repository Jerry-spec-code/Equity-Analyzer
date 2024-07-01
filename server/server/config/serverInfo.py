import os 
from dotenv import load_dotenv
load_dotenv()

PYTHON_ENV = os.environ.get('PYTHON_ENV')
DB_HOST = os.environ.get('DB_HOST')
DB_DATABASE = os.environ.get('DB_DATABASE')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
