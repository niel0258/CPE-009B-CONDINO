from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QLineEdit,QLabel
from register import RegisterApp
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterApp()
    window.show()
    sys.exit(app.exec())