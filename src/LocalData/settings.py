import base64

from cryptography.fernet import Fernet
from PyQt6.QtCore import QSettings


class AppSettings:
    def __init__(self):
        app_name = "GoldERP"
        organization = "AFT"

        self.settings = QSettings(organization, app_name)
        self.key = self._get_or_generate_key()

    def _get_or_generate_key(self):
        key = self.settings.value("encryption_key", type=str)
        if not key:
            key = base64.urlsafe_b64encode(Fernet.generate_key()).decode()
            self.settings.setValue("encryption_key", key)
        return base64.urlsafe_b64decode(key)

    def save_credentials(self, username, email, created_at):
        cipher = Fernet(self.key)

        encrypted_username = cipher.encrypt(username.encode()).decode()
        encrypted_email = cipher.encrypt(email.encode()).decode()
        encrypted_register_at = cipher.encrypt(created_at.encode()).decode()

        self.settings.setValue("username", encrypted_username)
        self.settings.setValue("email", encrypted_email)
        self.settings.setValue("created_at", encrypted_register_at)

        return "Credentials saved successfully."

    def update_credentials(self, username, email):
        cipher = Fernet(self.key)

        encrypted_username = cipher.encrypt(username.encode()).decode()
        encrypted_email = cipher.encrypt(email.encode()).decode()

        self.settings.setValue("username", encrypted_username)
        self.settings.setValue("email", encrypted_email)

        return "Credentials updated successfully."

    def load_credentials(self) -> tuple:
        cipher = Fernet(self.key)

        encrypted_username = self.settings.value("username", type=str)
        encrypted_email = self.settings.value("email", type=str)

        if encrypted_username or encrypted_email:
            username = cipher.decrypt(encrypted_username.encode()).decode()
            email = cipher.decrypt(encrypted_email.encode()).decode()
            return (username, email)
        return (None, None)

    def clear_credentials(self):
        self.settings.remove("username")
        self.settings.remove("email")
        self.settings.remove("created_at")
