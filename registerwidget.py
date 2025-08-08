from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow

class RegisterWidget(QWidget):
    def __init__(self,mainwindow):
        super().__init__()

        self.main_window = mainwindow

        label_username = QLabel("Username: ")
        line_edit_username = QLineEdit()

        label_password = QLabel("Password: ")
        line_edit_password = QLineEdit()

        label_confirm_password = QLabel("Confirm Password: ")
        line_edit_confirm_password = QLineEdit()

        label_phone = QLabel("Phone Number: ")
        line_edit_phone = QLineEdit()

        button_register = QPushButton("Register")
        button_register.clicked.connect(self.attemptRegister)
        
        button_cancel = QPushButton("Cancle")
        button_cancel.clicked.connect(mainwindow.switchToStartMenu)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_username)
        h_layout_1.addWidget(line_edit_username)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_password)
        h_layout_2.addWidget(line_edit_password)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(label_confirm_password)
        h_layout_3.addWidget(line_edit_confirm_password)

        h_layout_4 = QHBoxLayout()
        h_layout_4.addWidget(label_phone)
        h_layout_4.addWidget(line_edit_phone)
        
        h_layout_5 = QHBoxLayout()
        h_layout_5.addWidget(button_register)
        h_layout_5.addWidget(button_cancel)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)
        v_layout.addLayout(h_layout_4)
        v_layout.addLayout(h_layout_5)

        self.setLayout(v_layout)


    def attemptRegister(self):
        self.main_window.switchToStartMenu()

