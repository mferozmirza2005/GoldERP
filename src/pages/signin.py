from src.database_manager import DatabaseManager
from src.LocalData.settings import AppSettings
from PyQt6.QtGui import QCursor
from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QFormLayout,
    QMessageBox,
    QPushButton,
    QLineEdit,
    QWidget,
    QLabel,
)
from PyQt6.QtCore import Qt
import re


class SignIn(QWidget):
    def __init__(self, show_home, show_signup):
        super().__init__()
        self.show_home = show_home
        self.show_signup = show_signup
        self.settings = AppSettings()

        main_layout = QHBoxLayout()

        layout = QVBoxLayout()

        title_label = QLabel("SignIn")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; margin-top: 10px; margin-bottom: 30px;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        form_layout = QFormLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #111111;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
            }
            QLineEdit::placeholder {
                font-size: 18px;
                color: #888;
            }
        """
        )

        username_label = QLabel("Username:")
        username_label.setStyleSheet("font-size: 18px;")
        form_layout.addRow(username_label, self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Enter Password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #111111;
                border-radius: 5px;
                font-size: 16px;
                padding: 10px;
            }
            QLineEdit::placeholder {
                font-size: 18px;
                color: #888;
            }
        """
        )

        password_label = QLabel("Password:")
        password_label.setStyleSheet("font-size: 18px;")
        form_layout.addRow(password_label, self.password_input)

        self.submit_btn = QPushButton("Sign In")
        self.submit_btn.setFixedWidth(self.submit_btn.sizeHint().width() + 20)
        self.submit_btn.clicked.connect(self.signin_user)
        self.submit_btn.setStyleSheet(
            """
            QPushButton {
                background-color: #0078d4;
                border-radius: 5px;
                padding: 10px 20px;
                margin: 12px 0 0;
                font-size: 16px;
                cursor: pointer;
                color: white;
                border: none;
            }
            QPushButton:hover {
                background-color: #005ba1;
            }
        """
        )

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.submit_btn)
        button_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        form_layout.addRow(button_layout)

        signup_label = QLabel('<a href="#">Don\'t have an account? Sign Up here.</a>')
        signup_label.setStyleSheet(
            """
            QLabel {
                font-size: 14px;
                color: #0078d4;
            }
            QLabel:hover {
                color: #005ba1;
                text-decoration: underline;
            }
        """
        )
        signup_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        signup_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        signup_label.linkActivated.connect(self.show_signup)

        layout.addLayout(form_layout)
        layout.addWidget(signup_label)

        layout.addLayout(form_layout)

        layout.addStretch()
        main_layout.addStretch()
        main_layout.addLayout(layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def signin_user(self):
        try:
            db_manager = DatabaseManager()
        except Exception as e:
            return QMessageBox.warning(self, "Error", "Something wents wrong...")

        username = self.username_input.text()
        password = self.password_input.text()

        if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
            QMessageBox.warning(self, "Validation Error", "Username must be 3-20 characters long and alphanumeric.")
            return

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character."
            )
            return

        try:
            message = db_manager.verify_user(username, password)

            if message != "User matched successfully.":
                QMessageBox.warning(
                    self,
                    message,
                    "Please fill the valid details."
                )
                return

            self.username_input.clear()
            self.password_input.clear()

            user = db_manager.get_user(username)

            message = self.settings.save_credentials(username, user["email"], user["role"], user["created_at"])
            QMessageBox.information(self, "Success", message)
            self.show_home()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Got error in saving credentials: {e}")
