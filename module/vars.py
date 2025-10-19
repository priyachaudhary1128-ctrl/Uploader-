#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "23231900"))
API_HASH = environ.get("API_HASH", "d030150e323a1ff50851db2044cfe6ad")
BOT_TOKEN = environ.get("BOT_TOKEN", "8339041551:AAG1-JnDrDm-C3iJqzaEma6qYwd7u2nQEEk")

OWNER = int(environ.get("OWNER", "8463673971"))
CREDIT = environ.get("CREDIT", "BOBBY PIPPAL")
cookies_file_path = os.getenv("cookies_file_path", "youtube_cookies.txt")

TOTAL_USER = os.environ.get('TOTAL_USERS', '8463673971').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8463673971').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))



