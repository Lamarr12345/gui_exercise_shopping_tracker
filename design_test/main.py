from PySide6.QtWidgets import QApplication
from logicwidget import LogicWidget
import sys

def main():
    app = QApplication(sys.argv)

    logic_widget = LogicWidget()
    logic_widget.show()

    app.exec()

main()