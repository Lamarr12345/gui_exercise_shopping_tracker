from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow

class StartMenuWidget(QWidget):
    def __init__(self,mainwindow):
        super().__init__()

        #self.main_window = mainwindow

        button_register = QPushButton("Create Account")
        button_register.clicked.connect(mainwindow.switchToRegister)
        
        button_login = QPushButton("Log In")
        button_login.clicked.connect(mainwindow.switchToLogin)

        button_quit = QPushButton("Quit")
        button_quit.clicked.connect(mainwindow.quitApp)

        layout = QVBoxLayout()
        layout.addWidget(button_register)
        layout.addWidget(button_login)
        layout.addWidget(button_quit)
        self.setLayout(layout)


    #def goToRegisterPage(self):
    #    pass

    #def goToLoginPage(self):
    #    pass

    #def quitApp(self):
    #    self.main_window.quitApp()