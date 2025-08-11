from PySide6.QtWidgets import QWidget,QMessageBox,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow
from reportwindow import ReportWindow

class UserMenuWidget(QWidget):
    def __init__(self,mainwindow,datahandler):
        super().__init__()

        self.main_window = mainwindow
        self.data_handler = datahandler

        self.report_window = None

        button_add_item = QPushButton("Add Item Purchase")
        button_add_item.clicked.connect(mainwindow.switchToAddItem)
        
        button_report = QPushButton("Generate Report")
        button_report.clicked.connect(self.generateReport)

        button_logout = QPushButton("Log Out")
        button_logout.clicked.connect(self.logOut)

        button_logout_and_quit = QPushButton("Log Out and Quit")
        button_logout_and_quit.clicked.connect(self.logoutAndQuit)

        layout = QVBoxLayout()
        layout.addWidget(button_add_item)
        layout.addWidget(button_report)
        layout.addWidget(button_logout)
        layout.addWidget(button_logout_and_quit)
        self.setLayout(layout)

    def generateReport(self):
        if self.data_handler.checkIfCurrentUserPurchaseHistoryNotEmpty():
            self.report_window = ReportWindow(self.data_handler)
            self.report_window.show()
        else:
            QMessageBox.information(self,"No Purchases", "There are no purchases in the purchase history.\nPress 'Add Item Purchase' to add some.", QMessageBox.Ok)

    def logOut(self):
        self.data_handler.setCurrentUserLoggedIn(False)
        self.data_handler.freeCurrentUserData()
        self.main_window.switchToStartMenu()

    def logoutAndQuit(self):
        self.data_handler.setCurrentUserLoggedIn(False)
        self.main_window.quitApp()