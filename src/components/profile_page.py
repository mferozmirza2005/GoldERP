from PyQt6.QtWidgets import (
    QVBoxLayout,
    QWidget,
    QLabel
)

def profile_page():
    profile_layout = QVBoxLayout()
    profile_layout.setContentsMargins(0,0,0,0)
    profile_layout.setSpacing(0)

    main_widget = QWidget()
    main_widget.setLayout(profile_layout)

    home_label = QLabel("Profile page")
    profile_layout.addWidget(home_label)

    profile_layout.addStretch()

    return main_widget