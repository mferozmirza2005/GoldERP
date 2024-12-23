import datetime


class User:
    def __init__(self, username: str, email: str, password: str):
        if len(username) < 3 or len(username) > 20:
            raise ValueError("Username must be 3-20 characters long.")
        if not isinstance(email, str) or "@" not in email:
            raise ValueError("Invalid email address.")
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")

        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.datetime.now(datetime.UTC).isoformat()

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at,
        }
