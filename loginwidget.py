from PySide6.QtWidgets import QWidget,QMessageBox,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit
import time

#from mainwindow import MainWindow

class LoginWidget(QWidget):
    def __init__(self,mainwindow,datahandler):
        super().__init__()

        self.main_window = mainwindow
        self.data_handler = datahandler

        self.attempt_count = 3

        label_username = QLabel("Username: ")
        self.line_edit_username = QLineEdit()

        label_password = QLabel("Password: ")
        self.line_edit_password = QLineEdit()

        button_login = QPushButton("Log In")
        button_login.clicked.connect(self.attemptLogin)
        
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.cancelLogin)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_username)
        h_layout_1.addWidget(self.line_edit_username)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_password)
        h_layout_2.addWidget(self.line_edit_password)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(button_login)
        h_layout_3.addWidget(button_cancel)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)

        self.setLayout(v_layout)

    def attemptLogin(self):
        username = self.line_edit_username.text()
        password = self.line_edit_password.text()

        #check if input fields are empty
        missing_input_messages = []
        if not username:
            missing_input_messages.append("- username missing")
        if not password:
            missing_input_messages.append("- password missing")
        if missing_input_messages:
            QMessageBox.warning(self,"Missing inputs", "\n".join(missing_input_messages), QMessageBox.Ok)
            return

        #check if user even exists
        if not self.data_handler.checkIfUsernameTaken(username):
            QMessageBox.warning(self,"User not found", f"Username '{username}' not found.", QMessageBox.Ok)
            return
        
        #check password with attempt counterl logic
        if not self.data_handler.checkPasswordMatch(username,password):
            self.attempt_count = self.attempt_count - 1
            if self.attempt_count > 0:
                QMessageBox.warning(self,"Wrong password", f"You have '{self.attempt_count}' more {"tries" if self.attempt_count>1 else "try"}.", QMessageBox.Ok)
                self.line_edit_password.clear()
                return
            elif self.attempt_count == 0:
                QMessageBox.critical(self,"Wrong password", f"Back to the start menu.\nAfter next attempt the app will be closed.", QMessageBox.Ok)
                self.line_edit_password.clear()
                self.main_window.switchToStartMenu()
                return
            else:
                self.main_window.quitApp()
                return
        
        self.data_handler.setCurrentUserData(username)

        if self.data_handler.getCurrentUserLoggedIn():
            QMessageBox.warning(self,"Warning", "Not logged out properly last time.", QMessageBox.Ok)
        else:
            self.data_handler.setCurrentUserLoggedIn(True)

        self.attempt_count = 3
        self.line_edit_username.clear()
        self.line_edit_password.clear()
        self.main_window.switchToUserMenu()

    def cancelLogin(self):
        self.line_edit_username.clear()
        self.line_edit_password.clear()
        self.main_window.switchToStartMenu()