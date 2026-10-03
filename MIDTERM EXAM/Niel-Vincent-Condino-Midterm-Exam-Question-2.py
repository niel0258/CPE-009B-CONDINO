import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QWidget,QPushButton,QVBoxLayout
from PyQt6.QtCore import Qt

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Special Midterm Exam in OOP"
        self.size_x = 400
        self.size_y = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.size_x,self.size_y)

        self.button = QPushButton("Click to Change Color",self)
        self.button.setMaximumWidth(500)
        self.button.clicked.connect(self.btn_change_color)

        container = QWidget()

        layout = QVBoxLayout(container)

        layout.addWidget(self.button,alignment=Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(container)
        self.show()

    def btn_change_color(self):
        self.button.setStyleSheet(""" 
            background-color: yellow;
        """)



app = QApplication(sys.argv)
ex = App()
sys.exit(app.exec())