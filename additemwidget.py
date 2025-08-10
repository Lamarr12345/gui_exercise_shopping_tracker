from PySide6.QtWidgets import QWidget,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit

#from mainwindow import MainWindow

# - The date of the purchase (accept the following formats: MM/DD/YYYY, MM-DD-YYYY) but save the date as MM/DD/YYYY, 
# - The item purchased (should be a string of at least 3 characters), 
# - The total cost of the item (should be an integer or a float - including charges on delivery), 
# - The weight of the item( should be a float, and in kg)
# - The quantity purchased (should be an integer from 1 and above).

class AddItemWidget(QWidget):
    def __init__(self,mainwindow,datahandler):
        super().__init__()

        self.main_window = mainwindow
        self.data_handler = datahandler

        label_date = QLabel("Date of purchase: ")
        label_day = QLabel("Day")
        self.line_edit_day = QLineEdit()
        label_month = QLabel("Month")
        self.line_edit_month = QLineEdit()
        label_year = QLabel("Year")
        self.line_edit_year = QLineEdit()

        label_item_puchased = QLabel("Item purchased: ")
        self.line_edit_item_puchased = QLineEdit()

        label_item_cost = QLabel("Cost per item (in EUR): ")
        self.line_edit_item_cost = QLineEdit()

        label_item_weight = QLabel("Weight of item (in kg): ")
        self.line_edit_item_weight = QLineEdit()

        label_item_quantity = QLabel("Quantity of items: ")
        self.line_edit_item_quantity = QLineEdit()

        button_make_entry = QPushButton("Make Entry")
        button_make_entry.clicked.connect(self.attemptItemEntry)
        button_cancel = QPushButton("Cancel")
        button_cancel.clicked.connect(self.cancelItemEntry)


        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label_date)
        h_layout_1.addWidget(label_day)
        h_layout_1.addWidget(self.line_edit_day)
        h_layout_1.addWidget(label_month)
        h_layout_1.addWidget(self.line_edit_month)
        h_layout_1.addWidget(label_year)
        h_layout_1.addWidget(self.line_edit_year)

        h_layout_2 = QHBoxLayout()
        h_layout_2.addWidget(label_item_puchased)
        h_layout_2.addWidget(self.line_edit_item_puchased)

        h_layout_3 = QHBoxLayout()
        h_layout_3.addWidget(label_item_cost)
        h_layout_3.addWidget(self.line_edit_item_cost)

        h_layout_4 = QHBoxLayout()
        h_layout_4.addWidget(label_item_weight)
        h_layout_4.addWidget(self.line_edit_item_weight)

        h_layout_5 = QHBoxLayout()
        h_layout_5.addWidget(label_item_quantity)
        h_layout_5.addWidget(self.line_edit_item_quantity)

        h_layout_6 = QHBoxLayout()
        h_layout_6.addWidget(button_make_entry)
        h_layout_6.addWidget(button_cancel)

        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)
        v_layout.addLayout(h_layout_3)
        v_layout.addLayout(h_layout_4)
        v_layout.addLayout(h_layout_5)
        v_layout.addLayout(h_layout_6)
        self.setLayout(v_layout)


    def attemptItemEntry(self):
        self.main_window.switchToUserMenu()

    def cancelItemEntry(self):
        self.line_edit_day.clear()
        self.line_edit_month.clear()
        self.line_edit_year.clear()
        self.line_edit_item_puchased.clear()
        self.line_edit_item_cost.clear()
        self.line_edit_item_weight.clear()
        self.line_edit_item_quantity.clear()
        self.main_window.switchToUserMenu()