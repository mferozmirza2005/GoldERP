from pymongo.server_api import ServerApi
from pymongo.errors import PyMongoError
from pymongo import MongoClient
from models.user import User
from bson import ObjectId
import bcrypt


class DatabaseManager:
    def __init__(self):
        uri = "mongodb+srv://mferozmirza2005:vsdtRKE5boJHekaq@golderp.mvt4h.mongodb.net/?retryWrites=true&w=majority&appName=GoldERP"
        self.client = MongoClient(uri, server_api=ServerApi("1"))
        self.db = self.client["gold_erp"]

    def save_user(
        self, username: str, email: str, password: str, created_at: str
    ) -> str:
        try:
            users_collection = self.db["users"]
            if users_collection.find_one({"email": email}):
                raise Exception("A user with this email already exists.")
            
            salt = bcrypt.gensalt()
            salted_pwd = bcrypt.hashpw(password.encode("utf-8"), salt)

            user = {
                "username": username,
                "email": email,
                "password": salted_pwd,
                "role": "--",
                "approved": False,
                "created_at": created_at,
            }
            users_collection.insert_one(user)
            return "User successfully registered, Waiting for approval."
        except PyMongoError as e:
            return f"Failed to save user: {e}"

    def update_user(self, updated_username: str, updated_email: str, email: str) -> str:
        try:
            users_collection = self.db["users"]

            users_collection.update_one(
                {"_id": ObjectId(users_collection.find_one({"email": email})["_id"])},
                {"$set": {"username": updated_username, "email": updated_email}},
            )
            return "User successfully registered."
        except PyMongoError as e:
            return f"Failed to save user: {e}"

    def get_user(self, username: str) -> User | str:
        try:
            user = self.db["users"].find_one({"username": username})
            return user
        except Exception as e:
            return f"Failed to fetch user: {e}"

    def get_all_user(self) -> list | str:
        try:
            users = self.db["users"].find().to_list()
            return users
        except Exception as e:
            return f"Failed to fetch user: {e}"

    def verify_user(self, username: str, password: str) -> str:
        try:
            user = self.db["users"].find_one({"username": username})
            if not user or not bcrypt.checkpw(password.encode("utf-8"), user["password"]):
                return "Incorrect credentials."
            else:
                return "User matched successfully."
        except Exception as e:
            return f"Failed to verify user: {e}"

    def close_connection(self):
        if self.client:
            self.client.close()
