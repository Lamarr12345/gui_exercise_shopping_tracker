from PySide6.QtWidgets import QWidget,QStackedWidget,QMessageBox,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

from handledata import HandleData
from additemwidget import AddItemWidget
from loginwidget import LoginWidget
from registerwidget import RegisterWidget
from startmenuwidget import StartMenuWidget
from usermenuwidget import UserMenuWidget

class MainWindow(QWidget):
    def __init__(self,app):
        super().__init__()

        self.setWindowTitle("Purchase Tracker")

        self.app = app

        #initialize data handler object
        self.data_handler = HandleData(self)
        #initialize all widget frames
        self.star_menu = StartMenuWidget(self)
        self.register = RegisterWidget(self,self.data_handler)
        self.login = LoginWidget(self,self.data_handler)             
        self.user_menu = UserMenuWidget(self,self.data_handler)
        self.add_item = AddItemWidget(self,self.data_handler)

        #put widget frames into QStackWidget to switch between them later
        self.widget_stack = QStackedWidget(self)
        self.widget_stack.addWidget(self.star_menu)     #index 0 of stack
        self.widget_stack.addWidget(self.register)      #index 1 of stack
        self.widget_stack.addWidget(self.login)         #index 2 of stack
        self.widget_stack.addWidget(self.user_menu)     #index 3 of stack
        self.widget_stack.addWidget(self.add_item)      #index 4 of stack

        #setup mainwindow layout
        layout = QHBoxLayout(self)
        layout.addWidget(self.widget_stack)
        self.setLayout(layout)

        #switch to stat menu
        self.widget_stack.setCurrentIndex(0)

    def quitApp(self):
        self.app.quit()

    def switchToStartMenu(self):
        self.widget_stack.setCurrentIndex(0)

    def switchToRegister(self):
        self.widget_stack.setCurrentIndex(1)

    def switchToLogin(self):
        self.widget_stack.setCurrentIndex(2)

    def switchToUserMenu(self):
        self.widget_stack.setCurrentIndex(3)

    def switchToAddItem(self):
        self.widget_stack.setCurrentIndex(4)

