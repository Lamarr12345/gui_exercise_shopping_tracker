from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit
from datetime import date
from PySide6.QtCore import Qt

class ReportWindow(QWidget):
    def __init__(self,datahandler):
        super().__init__()

        username = datahandler.getCurrentUserData()["username"]
        phone_number = datahandler.getCurrentUserData()["user_data"]["phone_number"]
        purchase_history = datahandler.getCurrentUserData()["user_data"]["purchase_history"]

        label_headline = QLabel("PURCHASE EXPENSES REPORT")

        label_username = QLabel(username)
        label_phone_number = QLabel(phone_number)
        label_today = QLabel(date.today().isoformat())

        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_headline)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_username,1)
        h_layout_2.addWidget(label_phone_number,100)
        h_layout_2.addWidget(label_today,1)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        self.setLayout(v_layout)

