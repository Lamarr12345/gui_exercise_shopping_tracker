from PySide6.QtWidgets import QWidget,QStackedWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

from handledatafile import HandleDataFile
from additemwidget import AddItemWidget
from loginwidget import LoginWidget
from registerwidget import RegisterWidget
from startmenuwidget import StartMenuWidget
from usermenuwidget import UserMenuWidget

class MainWindow(QWidget):
    def __init__(self,app):
        super().__init__()

        self.setWindowTitle("Amazon Tracker")

        self.app = app

        self.star_menu = StartMenuWidget(self)          #index 0 of stack
        self.register = RegisterWidget(self)            #index 1 of stack
        self.login = LoginWidget(self)                  #index 2 of stack
        self.user_menu = UserMenuWidget(self)           #index 3 of stack
        self.add_item = AddItemWidget(self)             #index 4 of stack

        self.widget_stack = QStackedWidget(self)
        self.widget_stack.addWidget(self.star_menu)
        self.widget_stack.addWidget(self.register)
        self.widget_stack.addWidget(self.login)
        self.widget_stack.addWidget(self.user_menu)
        self.widget_stack.addWidget(self.add_item)

        layout = QHBoxLayout(self)
        layout.addWidget(self.widget_stack)

        self.setLayout(layout)

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

