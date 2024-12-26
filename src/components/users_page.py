from src.database_manager import DatabaseManager
from src.LocalData.settings import AppSettings
from PyQt6.QtWidgets import (
    QVBoxLayout,
    QTableView,
    QWidget,
    QLabel,
)
from PyQt6 import QtCore


class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data
        self.headers = ['Username', 'Email', 'Role', 'Created At']

    def data(self, index, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            user = self._data[index.row()]
            if index.column() == 0:
                return user['username']
            elif index.column() == 1:
                return user['email']
            elif index.column() == 2:
                return user['role']
            elif index.column() == 3:
                return user['created_at']
        return None

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self.headers)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return self.headers[section]
        return None


def users_page():
    database_manager = DatabaseManager()
    settings = AppSettings()

    username, email, role = settings.load_credentials()

    users = database_manager.get_all_user()
    
    users_list = []
    for user in users:
        if user["username"] != username and user["email"] != email or user["role"] != role:
            users_list.append(user)

    page_layout = QVBoxLayout()
    page_layout.setContentsMargins(0,0,0,0)
    page_layout.setSpacing(0)

    main_widget = QWidget()
    main_widget.setLayout(page_layout)

    page_label = QLabel("Users page")
    page_layout.addWidget(page_label)

    if len(users_list) > 0:
        model = TableModel(users_list)
        users_table = QTableView()
        users_table.setModel(model)

        page_layout.addWidget(users_table)

    page_layout.addStretch()

    return main_widget