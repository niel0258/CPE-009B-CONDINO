import sys
from PyQt6.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__() # initializes the main window like in the previous one
        # window = QMainWindow()
        self.title = "PyQt Button"
        self.window_x = 200 # or left
        self.window_y = 200 # or top
        self.window_width = 300
        self.window_height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.window_x, self.window_y, self.window_width, self.window_height)
        self.setWindowIcon(QIcon('pythonico.ico'))

        # In GUI Python, these buttons, textboxes, labels are called Widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hovered over me!")
        self.button.move(100, 70) # button.move(x,y)
        self.button.clicked.connect(self.on_click)

        self.show()
    
    @pyqtSlot()
    def on_click(self):
        print("Y-YO?! You clicked me?! W-What are you doing, idiot?! I-It’s not like I wanted you to click me or anything! Baka! 😤")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec())