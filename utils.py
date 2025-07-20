from config import ADMIN_IDS
import db

def is_admin(user_id):
    return int(user_id) in ADMIN_IDS

def user_balance(user_id):
    user = db.get_user(user_id)
    return user[3] if user else 0
