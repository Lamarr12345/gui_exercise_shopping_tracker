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

        shipping_rate = 1 #EUR/kg
        spending_limit = 500

        earliest_purchase = min([x["purchase_date"] for x in purchase_history],key = lambda y : date.fromisoformat(y))
        latest_purchase = max([x["purchase_date"] for x in purchase_history],key = lambda y : date.fromisoformat(y))

        total_item_cost = sum([x["item_price"]*x["item_quantity"] for x in purchase_history])
        total_delivery_cost = sum([x["item_weight"]*x["item_quantity"]*shipping_rate for x in purchase_history])
        total_cost = total_item_cost + total_delivery_cost

        most_expensive_item = max(purchase_history,key=lambda x : x["item_price"])
        least_expensive_item = min(purchase_history,key=lambda x : x["item_price"])

        average_cost = total_item_cost / sum([x["item_quantity"] for x in purchase_history])

        if total_cost > spending_limit:
            exceeded_spending_limit = True
        else:
            exceeded_spending_limit = False


        v_layout = QVBoxLayout()
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel("              PURCHASE EXPENSES REPORT"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"{username}                 {phone_number}              {today.isoformat()}"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"You have spend a total of {total_cost:.2f} EUR on Amazon purchases\n{"between "+earliest_purchase+" and "+latest_purchase if earliest_purchase != latest_purchase else "on "+latest_purchase}."))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"TOTAL ITEM COST:            {total_item_cost}"))
        v_layout.addWidget(QLabel(f"TOTAL DELIVERY COST:     {total_delivery_cost}"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"MOST EXPENSIVE:         {most_expensive_item["item_purchased"]}"))
        v_layout.addWidget(QLabel(f"Price per item:             {most_expensive_item["item_price"]}"))
        v_layout.addWidget(QLabel(f"Quantity bought:          {most_expensive_item["item_quantity"]}"))
        v_layout.addWidget(QLabel(f"Delivery cost per item: {(most_expensive_item["item_weight"]*shipping_rate):.2f}"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"LEAST EXPENSIVE:        {least_expensive_item["item_purchased"]}"))
        v_layout.addWidget(QLabel(f"Price per item:             {least_expensive_item["item_price"]}"))
        v_layout.addWidget(QLabel(f"Quantity bought:          {least_expensive_item["item_quantity"]}"))
        v_layout.addWidget(QLabel(f"Delivery cost per item: {(least_expensive_item["item_weight"]):.2f}"))
        v_layout.addWidget(QLabel(""))
        v_layout.addWidget(QLabel(f"AVERAGE ITEM COST:      {average_cost:.2f}"))
        v_layout.addWidget(QLabel(""))
        if exceeded_spending_limit:
            v_layout.addWidget(QLabel(f"The spending limit of {(spending_limit):.2f} EUR has been exceeded by {(total_cost-spending_limit):.2f} EUR."))
        else:
            v_layout.addWidget(QLabel(f"The spending limit of {(spending_limit):.2f} EUR has not been exceeded."))
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

