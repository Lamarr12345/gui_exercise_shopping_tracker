from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow
from reportwindow import ReportWindow

class UserMenuWidget(QWidget):
    def __init__(self,mainwindow):
        super().__init__()

        self.main_window = mainwindow

        self.report_window = None

        button_add_item = QPushButton("Add Purchase")
        #button_add_item.clicked.connect(mainwindow.switchToAddItem)
        
        button_report = QPushButton("Generate Report")
        button_report.clicked.connect(self.generateReport)

        button_quit = QPushButton("Quit and Log Out")
        button_quit.clicked.connect(self.quitAndLogout)

        layout = QVBoxLayout()
        layout.addWidget(button_add_item)
        layout.addWidget(button_report)
        layout.addWidget(button_quit)
        self.setLayout(layout)

    def quitAndLogout(self):
        #todo
        self.main_window.quitApp()

    def generateReport(self):
        self.report_window = ReportWindow()
        self.report_window.show()
