from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor

class Registration_Success:
    def __init__(self):
        self.widget = QWidget()

        self.success_heading = QLabel("Registration Successful!", self.widget)
        self.success_heading.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.success_heading.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        self.success_heading.setStyleSheet("color: #4CAF50;")

        self.success_message = QLabel(
            "Waiting for approval. You can't use the application until you get an email for your account approval.",
            self.widget
        )
        self.success_message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.success_message.setFont(QFont("Arial", 12))
        self.success_message.setStyleSheet("color: #555;")
        self.success_message.setWordWrap(True)

        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        layout.addWidget(self.success_heading)
        layout.addWidget(self.success_message)

        self.widget.setLayout(layout)

    def render_registration_success(self):
        return self.widget
