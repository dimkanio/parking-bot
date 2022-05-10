import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN = os.environ['TOKEN']
PARKING_CHAT_ID = os.environ['PARKING_CHAT_ID']
DBPATH = os.path.join(BASE_DIR, "db1e3bfkg2bidc")
DATABASE_URL = os.environ.get("DATABASE_URL")
HOME_URL = os.environ['HOME_URL']
SALT = os.environ['SALT']
LOGLEVEL = os.environ['LOGLEVEL']

