from PySide6.QtWidgets import QWidget,QPushButton,QLineEdit,QVBoxLayout
from logic import Logic

class LogicWidget(QWidget,Logic):
    def __init__(self):
        super().__init__()

        button_print_something = QPushButton("Print Something")
        button_print_something.clicked.connect(self.printSomething)
        line_edit = QLineEdit()
        button_print_text = QPushButton("Print Text")
        button_print_text.clicked.connect(lambda : self.printText(line_edit.text()))
        #button_print_text.clicked.connect(lambda : (self.printText(line_edit.text(),line_edit.clear())))

        v_layout = QVBoxLayout()
        v_layout.addWidget(button_print_something)
        v_layout.addWidget(line_edit)
        v_layout.addWidget(button_print_text)
        self.setLayout(v_layout)

