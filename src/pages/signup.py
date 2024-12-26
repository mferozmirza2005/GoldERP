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
from models.user import User
from PyQt6.QtCore import Qt
import re


class SignUp(QWidget):
    def __init__(self, show_registration_success, show_signin):
        super().__init__()

        self.show_registration_success = show_registration_success
        self.show_signin = show_signin
        self.settings = AppSettings()

        main_layout = QHBoxLayout()

        layout = QVBoxLayout()

        title_label = QLabel("Create An Account")
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

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")
        self.email_input.setStyleSheet(
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

        email_label = QLabel("Email:")
        email_label.setStyleSheet("font-size: 18px;")
        form_layout.addRow(email_label, self.email_input)

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

        self.submit_btn = QPushButton("Sign Up")
        self.submit_btn.setFixedWidth(self.submit_btn.sizeHint().width() + 20)
        self.submit_btn.clicked.connect(self.register_user)
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

        signin_label = QLabel('<a href="#">Already have an account? Sign In here.</a>')
        signin_label.setStyleSheet(
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
        signin_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        signin_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        signin_label.linkActivated.connect(self.show_signin)

        layout.addLayout(form_layout)
        layout.addWidget(signin_label)

        layout.addStretch()
        main_layout.addStretch()
        main_layout.addLayout(layout)
        main_layout.addStretch()

        self.setLayout(main_layout)

    def register_user(self):
        try:
            db_manager = DatabaseManager()
        except Exception as e:
            return QMessageBox.warning(self, "Error", "Something wents wrong...")

        username = self.username_input.text()
        email = self.email_input.text()
        password = self.password_input.text()

        if not re.match(r"^[a-zA-Z0-9]{3,20}$", username):
            QMessageBox.warning(self, "Validation Error", "Username must be 3-20 characters long and alphanumeric.")
            return

        if not re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            QMessageBox.warning(self, "Validation Error", "Invalid email address format.")
            return

        if not re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
            QMessageBox.warning(
                self,
                "Validation Error",
                "Password must be at least 8 characters long, include uppercase, lowercase, a number, and a special character."
            )
            return

        try:
            self.username_input.clear()
            self.email_input.clear()
            self.password_input.clear()

            user = User(username, email, password).to_dict()

            message = db_manager.save_user(username, email, password, user["created_at"])
            self.show_registration_success()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Got error in saving credentials: {e}")
