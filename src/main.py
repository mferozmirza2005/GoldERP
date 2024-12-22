import sys

from PyQt6.QtWidgets import (
    QStackedWidget,
    QApplication,
    QMainWindow,
    QMenu,
)

from src.LocalData.settings import AppSettings
from src.pages.home import Home
from src.pages.signin import SignIn
from src.pages.signup import SignUp


class AddMenu(QMenu):
    def mouseReleaseEvent(self, event):
        self.triggered.emit(None)
        super().mouseReleaseEvent(event)


class GoldERP(QMainWindow):
    def __init__(self):
        super().__init__()

        self.settings = AppSettings()
        self.setWindowTitle("Gold ERP")

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.stacked_widget.setContentsMargins(0,0,0,0)

        self.home_page = Home()
        self.signin_page = SignIn(self.show_home, self.show_signup)
        self.signup_page = SignUp(self.show_home, self.show_signin)

        self.stacked_widget.addWidget(self.home_page)
        self.stacked_widget.addWidget(self.signin_page)
        self.stacked_widget.addWidget(self.signup_page)

        self.show_home()
        self.create_menu_bar()
        self.showMaximized()

    def create_menu_bar(self):
        menubar = self.menuBar()

        HomeMenu = AddMenu("Home", self)
        HomeMenu.triggered.connect(self.show_home)
        menubar.addMenu(HomeMenu)

    def show_home(self):
        username = self.settings.load_credentials()

        self.stacked_widget.setCurrentWidget(self.home_page)
        home_button = self.home_page.render_home()

        if not username:
            self.stacked_widget.addWidget(self.signin_page)
            home_button.clicked.connect(self.show_signin)
        else:
            home_button.clicked.connect(self.logout_user)

    def show_signin(self):
        self.stacked_widget.setCurrentWidget(self.signin_page)

    def show_signup(self):
        self.stacked_widget.setCurrentWidget(self.signup_page)

    def logout_user(self):
        self.settings.clear_credentials()
        self.show_signin()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = GoldERP()

    sys.exit(app.exec())