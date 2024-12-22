from PyQt6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QWidget,
)

from src.LocalData.settings import AppSettings


class Home(QWidget):
    """Home Page Widget"""

    def __init__(self):
        super().__init__()
        self.settings = AppSettings()

    def render_home(self):
        try:
            if self.layout():
                QWidget().setLayout(self.layout())

            main_layout = QHBoxLayout()

            nav_bar = QVBoxLayout()
            nav_bar.setContentsMargins(0, 0, 0, 0)
            nav_bar.setSpacing(0)

            username = self.settings.load_credentials()

            button_style = """
                QPushButton {
                    background-color: #616161;
                    color: white;
                    border: none;
                    padding: 15px 20px;
                    text-align: left;
                }
                QPushButton:hover {
                    background-color: #3B3B3B;
                }
                QPushButton:pressed {
                    background-color: #3B3B3B;
                }
            """

            btn_profile = QPushButton("Profile")
            btn_profile.setStyleSheet(button_style)
            nav_bar.addWidget(btn_profile)

            if not username:
                signin_btn = QPushButton("SignIn")
                signin_btn.setStyleSheet(button_style)
                nav_bar.addWidget(signin_btn)

                nav_bar.addStretch()
                nav_widget = QWidget()
                nav_widget.setLayout(nav_bar)
                nav_widget.setFixedWidth(150)
                nav_widget.setContentsMargins(0,0,0,0)
                nav_widget.setStyleSheet("background-color: #424242;")

                main_layout.addWidget(nav_widget)
                main_layout.addStretch()
                self.setLayout(main_layout)

                return signin_btn
            else:
                logout_btn = QPushButton("Logout")
                logout_btn.setStyleSheet(button_style)
                nav_bar.addWidget(logout_btn)

                nav_bar.addStretch()
                nav_widget = QWidget()
                nav_widget.setLayout(nav_bar)
                nav_widget.setFixedWidth(150)
                nav_widget.setContentsMargins(0,0,0,0)
                nav_widget.setStyleSheet("background-color: #424242;")

                main_layout.addWidget(nav_widget)
                main_layout.addStretch()
                self.setLayout(main_layout)

                return logout_btn
        except Exception as e:
            print(e)
