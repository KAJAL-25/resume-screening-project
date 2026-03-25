import sqlite3

def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def check_login(username, password):
    return username == "admin" and password == "admin"
from database import add_user, check_user

def signup_user(username, password):
    if not username or not password:
        return False, "Username and password cannot be empty"

    success = add_user(username, password)

    if success:
        return True, "Signup successful"
    else:
        return False, "Username already exists"

def login_user(username, password):
    if not username or not password:
        return False

    return check_user(username, password)
