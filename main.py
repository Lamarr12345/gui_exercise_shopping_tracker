from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

main_window = MainWindow(app)
main_window.show()

app.exec()