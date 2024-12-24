from src.database_manager import DatabaseManager
from src.LocalData.settings import AppSettings
from PyQt6.QtWidgets import (
    QSizePolicy,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QFormLayout,
    QLineEdit,
    QWidget,
    QLabel,
)


class Profile:
    def __init__(self):
        self.database_manager = DatabaseManager()
        self.settings = AppSettings()
        self.main_widget = QWidget()

        self.profile_layout = QVBoxLayout()
        self.profile_layout.setContentsMargins(0, 0, 0, 0)
        self.profile_layout.setSpacing(0)

        self.main_widget.setLayout(self.profile_layout)

        self.profile_heading = QLabel("Your Profile")
        self.profile_heading.setStyleSheet(
            """
            padding: 0px 30px 25px;
            font-weight: bold;
            font-size: 24px;
        """
        )
        self.profile_layout.addWidget(self.profile_heading)

        self.username, self.email = self.settings.load_credentials()

        self.username_label = QLabel(f"User Name: {self.username}")
        self.email_label = QLabel(f"Email: {self.email}")

        self.label_style = """
            padding: 10px 30px 0px;
            font-size: 16px;
        """

        self.username_label.setStyleSheet(self.label_style)
        self.email_label.setStyleSheet(self.label_style)

        self.profile_layout.addWidget(self.username_label)
        self.profile_layout.addWidget(self.email_label)

        self.edit_btn = QPushButton("EDIT")
        self.edit_btn.setStyleSheet(
            """
            background-color: #1F51FF;
            margin: 30px 30px 0px;
            border-radius: 15px;
            padding: 10px 25px;
            text-align: left;
            font-size: 16px;
            border: none;
            color: white;
        """
        )
        self.edit_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.profile_layout.addWidget(self.edit_btn)

        self.edit_btn.clicked.connect(lambda: self.edit_profile())

        self.profile_layout.addStretch()

    def profile_page(self):
        return self.main_widget

    def edit_profile(self):
        self.username_label.setParent(None)
        self.email_label.setParent(None)
        self.edit_btn.setParent(None)

        self.profile_heading.setText("Edit Profile")

        self.form_layout = QFormLayout()

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setText(self.username)
        self.username_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #111111;
                margin: 25px 0px 0px;
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
        self.username_input.setFixedWidth(self.username_input.sizeHint().width() + 100)

        self.username_edit_label = QLabel("Username:")
        self.username_edit_label.setStyleSheet(
            """
            font-size: 18px;
            padding: 30px 30px 15px;
            """
        )
        self.form_layout.addRow(self.username_edit_label, self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")
        self.email_input.setText(self.email)
        self.email_input.setStyleSheet(
            """
            QLineEdit {
                background-color: #111111;
                margin: 10px 0px 0px;
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
        self.email_input.setFixedWidth(self.email_input.sizeHint().width() + 100)

        self.email_edit_label = QLabel("Email:")
        self.email_edit_label.setStyleSheet(
            """
            font-size: 18px;
            padding: 10px 30px 0px;
            """
        )
        self.form_layout.addRow(self.email_edit_label, self.email_input)

        button_style = """
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

        self.save_btn = QPushButton("Save")
        self.save_btn.setFixedWidth(self.save_btn.sizeHint().width() + 20)
        self.save_btn.setStyleSheet(button_style)
        self.save_btn.clicked.connect(lambda: self.save_edit())

        self.save_btn_layout = QVBoxLayout()
        self.save_btn_layout.addWidget(self.save_btn)

        self.save_btn_layout.setSpacing(0)

        self.save_btn_layout.setContentsMargins(50, 10, 0, 0)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.setFixedWidth(self.cancel_btn.sizeHint().width() + 20)
        self.cancel_btn.setStyleSheet(button_style)
        self.cancel_btn.clicked.connect(lambda: self.cancel_edit())

        self.cancel_btn_layout = QVBoxLayout()
        self.cancel_btn_layout.addWidget(self.cancel_btn)

        self.cancel_btn_layout.setSpacing(0)

        self.cancel_btn_layout.setContentsMargins(20, 10, 0, 0)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addLayout(self.save_btn_layout)
        self.buttons_layout.addLayout(self.cancel_btn_layout)

        self.form_layout.addRow(self.buttons_layout)

        self.profile_layout.addLayout(self.form_layout, 1)

    def cancel_edit(self):
        self.profile_heading.setText("Your Profile")

        self.username_edit_label.setParent(None)
        self.cancel_btn_layout.setParent(None)
        self.email_edit_label.setParent(None)
        self.save_btn_layout.setParent(None)
        self.username_input.setParent(None)
        self.buttons_layout.setParent(None)
        self.email_input.setParent(None)
        self.form_layout.setParent(None)
        self.cancel_btn.setParent(None)
        self.save_btn.setParent(None)

        self.profile_layout.insertWidget(1, self.username_label)
        self.profile_layout.insertWidget(2, self.email_label)
        self.profile_layout.insertWidget(3, self.edit_btn)

    def save_edit(self):
        updated_username = self.username_input.text()
        updated_email = self.email_input.text()

        if not updated_username or updated_username.strip() == "" and not updated_email or updated_email.strip() == "":
            return
        elif updated_username == self.username and updated_email == self.email:
            return
        

        try:
            self.database_manager.update_user(
                updated_username, updated_email, self.email
            )
            self.settings.update_credentials(updated_username, updated_email)

            self.username = updated_username
            self.email = updated_email

            self.username_label.setText(f"User Name: {self.username}")
            self.email_label.setText(f"User Name: {self.email}")

            self.profile_heading.setText("Your Profile")

            self.username_edit_label.setParent(None)
            self.cancel_btn_layout.setParent(None)
            self.email_edit_label.setParent(None)
            self.save_btn_layout.setParent(None)
            self.username_input.setParent(None)
            self.buttons_layout.setParent(None)
            self.email_input.setParent(None)
            self.form_layout.setParent(None)
            self.cancel_btn.setParent(None)
            self.save_btn.setParent(None)

            self.profile_layout.insertWidget(1, self.username_label)
            self.profile_layout.insertWidget(2, self.email_label)
            self.profile_layout.insertWidget(3, self.edit_btn)
        except Exception as e:
            return e
