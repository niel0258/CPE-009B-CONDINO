import sys
from PyQt6.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = "PyQt Button"
        self.window_x = 200
        self.window_y = 200
        self.window_width = 300
        self.window_height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.window_x, self.window_y, self.window_width, self.window_height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 70)
        self.button.clicked.connect(self.on_click)

        self.show()
    
    @pyqtSlot()
    def on_click(self):
        # PyQt6 uses QMessageBox.StandardButton for buttons
        buttonReply = QMessageBox.question(
            self, 
            "Testing Response", 
            "Do you still love her?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if buttonReply == QMessageBox.StandardButton.Yes:
            QMessageBox.warning(
                self, 
                "Evaluation", 
                "User clicked Yes", 
                QMessageBox.StandardButton.Ok
            )
        else:
            QMessageBox.information(
                self, 
                "Evaluation", 
                "User clicked No", 
                QMessageBox.StandardButton.Ok
            )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())