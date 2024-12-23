from PyQt6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel
)

def main_page():
    page_layout = QVBoxLayout()
    page_layout.setContentsMargins(0,0,0,0)
    page_layout.setSpacing(0)

    main_widget = QWidget()
    main_widget.setLayout(page_layout)

    home_label = QLabel("Home page")
    page_layout.addWidget(home_label)

    page_layout.addStretch()

    return main_widget