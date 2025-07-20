import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))
PAYMENT_NUMBERS = {
    "bkash": os.getenv("BKASH_NUMBER", "017XXXXXXXX"),
    "nagad": os.getenv("NAGAD_NUMBER", "018XXXXXXXX"),
}
DB_NAME = "data.sqlite3"
