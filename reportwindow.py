from PySide6.QtWidgets import QWidget,QTextEdit,QComboBox,QTabWidget,QSpacerItem,QListWidget,QAbstractItemView,QGroupBox,QCheckBox,QRadioButton,QButtonGroup,QLabel,QGridLayout,QVBoxLayout,QHBoxLayout,QPushButton,QSizePolicy,QLineEdit
from datetime import date
from PySide6.QtCore import Qt

class ReportWindow(QWidget):
    def __init__(self,userdata):
        super().__init__()

        self.setWindowTitle("Purchase Report")

        username = userdata["username"]
        phone_number = userdata["user_data"]["phone_number"]
        purchase_history = userdata["user_data"]["purchase_history"]
        today = date.today()



        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel("         PURCHASE EXPENSES REPORT"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"{username}                {phone_number}              {today.isoformat()}"))
        v_layout.addWidget(QLabel(""))
        # v_layout.addWidget(QLabel(f"You have spend a total of {total_cost} EUR on Amazon purchases {"between "+earliest_purchase+" and "+latest_purchase if earliest_purchase != latest_purchase else "on "+latest_purchase}."))
        # v_layout.addWidget(QLabel(""))
        # v_layout.addWidget(QLabel(f"TOTAL ITEM COST         {total_item_cost} (excluding delivery)"))
        # v_layout.addWidget(QLabel(f"TOTAL DELIVERY COST     {total_delivery_cost}"))
        # v_layout.addWidget(QLabel(""))
        # v_layout.addWidget(QLabel(f"MOST EXPENSIVE:         {most_expensive_item["item_purchased"]}"))
        # v_layout.addWidget(QLabel(f"Price per item:         {most_expensive_item["item_price"]} (including delivery)"))
        # v_layout.addWidget(QLabel(f"Quantity bought:        {most_expensive_item["item_quantity"]}"))
        # v_layout.addWidget(QLabel(f"Delivery cost per item: {round(most_expensive_item["item_weight"]*delivery_weight_cost,2)}"))
        # v_layout.addWidget(QLabel(""))
        # v_layout.addWidget(QLabel(f"LEAST EXPENSIVE:        {least_expensive_item["item_purchased"]}"))
        # v_layout.addWidget(QLabel(f"Price per item:         {least_expensive_item["item_price"]} (including delivery)"))
        # v_layout.addWidget(QLabel(f"Quantity bought:        {least_expensive_item["item_quantity"]}"))
        # v_layout.addWidget(QLabel(f"Delivery cost per item: {round(least_expensive_item["item_weight"]*delivery_weight_cost,2)}"))
        # v_layout.addWidget(QLabel(""))
        # v_layout.addWidget(QLabel(f"AVERAGE ITEMM COST      {average_cost} (including delivery)"))
        # v_layout.addWidget(QLabel(""))
        # if exceeded_spending_limit:
        #     v_layout.addWidget(QLabel(f"The spending limit of {spending_limit} EUR has been exceeded by {total_cost-spending_limit} EUR."))
        # else:
        #     v_layout.addWidget(QLabel(f"The spending limit of {spending_limit} EUR has not been exceeded."))
        # print("---------------------------------------------------------------------------")
        self.setLayout(v_layout)


        # html_text_edit = QTextEdit()
        # html_text_edit.setTextInteractionFlags(Qt.NoTextInteraction) 

        # html_text_edit.setHtml(f"<h1>Purchase Report</h1>{username}")

        # h_layout = QHBoxLayout()
        # h_layout.addWidget(html_text_edit)
        # self.setLayout(h_layout)


        # label_headline = QLabel("PURCHASE EXPENSES REPORT")

        # label_username = QLabel(username)
        # label_phone_number = QLabel(phone_number)
        # label_today = QLabel(date.today().isoformat())

        # h_layout_1 = QHBoxLayout()
        # h_layout_1.addWidget(label_headline)

        # h_layout_2 = QHBoxLayout()
        # h_layout_2.addWidget(label_username,1)
        # h_layout_2.addWidget(label_phone_number,100)
        # h_layout_2.addWidget(label_today,1)

        # v_layout = QVBoxLayout()
        # v_layout.addLayout(h_layout_1)
        # v_layout.addLayout(h_layout_2)
        # self.setLayout(v_layout)

