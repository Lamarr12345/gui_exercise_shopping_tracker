from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit,QMessageBox
import re

#from mainwindow import MainWindow

class RegisterWidget(QWidget):
    def __init__(self,mainwindow,datahandler):
        super().__init__()

        self.main_window = mainwindow
        self.data_handler = datahandler

        label_username = QLabel("Username: ")
        self.line_edit_username = QLineEdit()

        label_password = QLabel("Password: ")
        self.line_edit_password = QLineEdit()

        label_confirm_password = QLabel("Confirm Password: ")
        self.line_edit_confirm_password = QLineEdit()

        label_phone = QLabel("Phone Number: ")
        self.line_edit_phone = QLineEdit()

        button_register = QPushButton("Register")
        button_register.clicked.connect(self.attemptRegister)
        
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.cancelRegister)

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_username)
        h_layout_1.addWidget(self.line_edit_username)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_password)
        h_layout_2.addWidget(self.line_edit_password)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(label_confirm_password)
        h_layout_3.addWidget(self.line_edit_confirm_password)

        h_layout_4 = QHBoxLayout()
        h_layout_4.addWidget(label_phone)
        h_layout_4.addWidget(self.line_edit_phone)
        
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

        #check if input fields are empty
        missing_input_messages = []
        if not self.line_edit_username.text():
            missing_input_messages.append("- username missing")
        if not self.line_edit_password.text():
            missing_input_messages.append("- password missing")
        if not self.line_edit_confirm_password.text():
            missing_input_messages.append("- password confirmation missing")
        if not self.line_edit_phone.text():
            missing_input_messages.append("- phone number missing")
        if missing_input_messages:
            QMessageBox.warning(self,"Missing inputs", "\n".join(missing_input_messages), QMessageBox.Ok)
            return
        
        #check for empty spaces
        empty_space_messages = []
        if re.search(r" ",self.line_edit_username.text()):
            empty_space_messages.append("- username has empty space(s)")
        if re.search(r" ",self.line_edit_password.text()):
            empty_space_messages.append("- password has empty space(s)")
        if empty_space_messages:
            QMessageBox.warning(self,"Empty spaces", "\n".join(empty_space_messages), QMessageBox.Ok)
            return

        #check if user already exists
        if self.data_handler.checkIfUsernameTaken(self.line_edit_username.text()):
            QMessageBox.warning(self,"Username taken", "Username already taken.", QMessageBox.Ok)
            return
        
        #check password conditions
        pattern_length = r".{6,20}"
        pattern_upper = r"[A-Z]"
        pattern_lower = r"[a-z]"
        pattern_digit = r"[0-9]"
        pattern_special = r"[@$!%*#?&.,;:]"
        password_errors = []
        if not re.search(pattern_length,self.line_edit_password.text()):
            password_errors.append("- must be 6 to 20 characters long")
        if not re.search(pattern_upper,self.line_edit_password.text()):
            password_errors.append("- must contain at least one uppercase letter")
        if not re.search(pattern_lower,self.line_edit_password.text()):
            password_errors.append("- must contain at least one lowercase letter")
        if not re.search(pattern_digit,self.line_edit_password.text()):
            password_errors.append("- must contain at least one digit")
        if not re.search(pattern_special,self.line_edit_password.text()):
            password_errors.append("- must contain at least one special character (@$!%*#?&.,;:)")
        if self.line_edit_password.text() != self.line_edit_confirm_password.text():
            password_errors.append("- password and password confirmation do not match")
        if password_errors:
            QMessageBox.warning(self,"Password errors", "\n".join(password_errors), QMessageBox.Ok)
            return

        #check valid phone number
        phone_number = self.line_edit_phone.text().replace(" ","").replace("-","").replace("/","")
        pattern_phone = r"^\+49[0-9]{3,15}$"
        if not re.search(pattern_phone,phone_number):
            QMessageBox.warning(self,"Invalid phone number", "Invalid phone number.\n- german phone number(starts with +49)\n- between 3 and 15 numbers long", QMessageBox.Ok)
            return
        
        #add user to database
        self.data_handler.addUserToDataBaseUserBase(self.line_edit_username.text(),self.line_edit_password.text(),phone_number)

        QMessageBox.information(self,"Success", f"Account for user '{self.line_edit_username.text()}' successfully created!", QMessageBox.Ok)

        self.line_edit_username.clear()
        self.line_edit_password.clear()
        self.line_edit_confirm_password.clear()
        self.line_edit_phone.clear()

        self.main_window.switchToStartMenu()

    def cancelRegister(self):
        self.line_edit_username.clear()
        self.line_edit_password.clear()
        self.line_edit_confirm_password.clear()
        self.line_edit_phone.clear()
        self.main_window.switchToStartMenu()

