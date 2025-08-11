from PySide6.QtWidgets import QWidget,QMessageBox,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit
from datetime import date
import re

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

        day = self.line_edit_day.text()
        month = self.line_edit_month.text()
        year = self.line_edit_year.text()
        item_purchased = self.line_edit_item_puchased.text()
        item_cost = self.line_edit_item_cost.text()
        item_weight = self.line_edit_item_weight.text()
        item_quantity = self.line_edit_item_quantity.text()

        #check if input fields are empty
        missing_input_messages = []
        if not day:
            missing_input_messages.append("- day entry missing")
        if not month:
            missing_input_messages.append("- month entry missing")
        if not year:
            missing_input_messages.append("- year entry missing")
        if not item_purchased:
            missing_input_messages.append("- item purchased entry missing")
        if not item_cost:
            missing_input_messages.append("- item cost entry missing")
        if not item_weight:
            missing_input_messages.append("- item weight entry missing")
        if not item_quantity:
            missing_input_messages.append("- item quantity entry missing")
        if missing_input_messages:
            QMessageBox.warning(self,"Missing inputs", "\n".join(missing_input_messages), QMessageBox.Ok)
            return
        
        #check for input type errors
        input_type_errors = []
        try:
            day = int(day)
        except Exception:
            input_type_errors.append("- day has wrong type: integer (eg '3')")
        try:
            month = int(month)
        except Exception:
            input_type_errors.append("- month has wrong type: integer (eg '3')")
        try:
            year = int(year)
        except Exception:
            input_type_errors.append("- year has wrong type: integer (eg '2000')")
        try:
            item_cost = float(item_cost)
        except Exception:
            input_type_errors.append("- item cost has wrong type: float (eg '3.2' or '3')")
        try:
            item_weight = float(item_weight)
        except Exception:
            input_type_errors.append("- item weight has wrong type: float (eg '3.2' or '3')")
        try:
            item_quantity = int(item_quantity)
        except Exception:
            input_type_errors.append("- item quantity has wrong type: integer (eg '3')")
        if input_type_errors:
            QMessageBox.warning(self,"Input type error", "\n".join(input_type_errors), QMessageBox.Ok)
            return
        
        try:
            date_obj = date(year,month,day)
        except Exception:
            QMessageBox.warning(self,"Date error", "Invalid date.\nyear: MINYEAR <= year <= MAXYEAR\nmonth: 1 <= month <= 12\nday: 1 <= day <= number of days in the given month and year", QMessageBox.Ok)
            return

        other_errors = []
        if date_obj > date.today():
            other_errors.append("- date lies in the future")
        if re.search(r"^ +$",item_purchased):
            other_errors.append("- item purchased consists only of empty space(s)")
        if not item_cost > 0:
            other_errors.append("- item cost has to be positive decimal number (>0)")
        if not item_weight >= 0:
            other_errors.append("- item weight has to be not negative decimal number (>=0)")
        if not item_quantity >= 1:
            other_errors.append("- item quantity has to be at least 1")
        if other_errors:
            QMessageBox.warning(self,"Other errors", "\n".join(other_errors), QMessageBox.Ok)
            return
        
        self.data_handler.addItemToCurrentUserPurchaseHistory(date_obj.isoformat(),item_purchased,item_cost,item_weight,item_quantity)

        QMessageBox.information(self,"Success", f"Entry for '{item_purchased}' successfully created!", QMessageBox.Ok)

        self.line_edit_day.clear()
        self.line_edit_month.clear()
        self.line_edit_year.clear()
        self.line_edit_item_puchased.clear()
        self.line_edit_item_cost.clear()
        self.line_edit_item_weight.clear()
        self.line_edit_item_quantity.clear()
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