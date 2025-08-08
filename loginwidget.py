from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow

class LoginWidget(QWidget):
    def __init__(self,mainwindow):
        super().__init__()

        self.main_window = mainwindow

        label_username = QLabel("Username: ")
        line_edit_username = QLineEdit()

        label_password = QLabel("Password: ")
        line_edit_password = QLineEdit()

        button_login = QPushButton("Log In")
        button_login.clicked.connect(self.attemptLogin)
        
        button_cancel = QPushButton("Cancle")
        button_cancel.clicked.connect(mainwindow.switchToStartMenu)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_username)
        h_layout_1.addWidget(line_edit_username)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_password)
        h_layout_2.addWidget(line_edit_password)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(button_login)
        h_layout_3.addWidget(button_cancel)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)

        self.setLayout(v_layout)

    def attemptLogin(self):
        self.main_window.switchToUserMenu()