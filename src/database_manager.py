from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
from pymongo import MongoClient
from models.user import User


class DatabaseManager:
    def __init__(self):
        uri = "mongodb+srv://mferozmirza2005:vsdtRKE5boJHekaq@golderp.mvt4h.mongodb.net/?retryWrites=true&w=majority&appName=GoldERP"
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        self.db = self.client["gold_erp"]


    def save_user(self, username: str, email: str, password: str, created_at: str) -> str:
        try:
            users_collection = self.db["users"]
            if users_collection.find_one({"email": email}):
                raise Exception("A user with this email already exists.")
            user = {
                "username": username,
                "email": email,
                "password": password,
                "created_at": created_at,
            }
            users_collection.insert_one(user)
            return "User successfully registered."
        except PyMongoError as e:
            return f"Failed to save user: {e}"

    def get_user(self, username: str) -> User | str:
        try:
            user = self.db["users"].find_one({"username": username})
            return user
        except Exception as e:
            return f"Failed to fetch user: {e}"

    def verify_user(self, username: str, password: str) -> str:
        try:
            user = self.db["users"].find_one({"username": username})
            if not user or user["password"] != password:
                return "Incorrect credentials."
            else:
                return "User matched successfully."
        except Exception as e:
            return f"Failed to verify user: {e}"

    def close_connection(self):
        if self.client:
            self.client.close()
