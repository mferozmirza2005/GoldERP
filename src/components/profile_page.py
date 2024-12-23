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
from PyQt6.QtCore import Qt


class Profile:
    def __init__(self):
        self.settings = AppSettings()
        self.profile_layout = QVBoxLayout()
        self.profile_layout.setContentsMargins(0, 0, 0, 0)
        self.profile_layout.setSpacing(0)

        self.main_widget = QWidget()
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
        """)
        self.edit_btn.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        self.profile_layout.addWidget(self.edit_btn)

        self.edit_btn.clicked.connect(lambda: self.edit_profile())

        self.profile_layout.addStretch()

    def profile_page(self):
        return self.main_widget

    def edit_profile(self):
        self.profile_layout.removeWidget(self.username_label)
        self.username_label.deleteLater()
        self.username_label = None

        self.profile_layout.removeWidget(self.email_label)
        self.email_label.deleteLater()
        self.email_label = None

        self.profile_layout.removeWidget(self.edit_btn)
        self.edit_btn.deleteLater()
        self.edit_btn = None

        form_layout = QFormLayout()
        
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Enter Username")
        self.username_input.setText(self.username)
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
        self.username_input.setFixedWidth(self.username_input.sizeHint().width() + 100)

        username_label = QLabel("Username:")
        username_label.setStyleSheet("font-size: 18px;")
        form_layout.addRow(username_label, self.username_input)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter Email")
        self.email_input.setText(self.email)
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
        self.email_input.setFixedWidth(self.email_input.sizeHint().width() + 100)

        email_label = QLabel("Email:")
        email_label.setStyleSheet("font-size: 18px;")
        form_layout.addRow(email_label, self.email_input)

        self.submit_btn = QPushButton("Save")
        self.submit_btn.setFixedWidth(self.submit_btn.sizeHint().width() + 20)
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

        self.profile_layout.insertLayout(1, form_layout)