from PyQt6.QtWidgets import QWidget
import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QLabel,QPushButton,QGridLayout,QVBoxLayout,QLineEdit

class NameApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Midterm in OOP"
        self.size_x = 600
        self.size_y = 400
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setFixedSize(self.size_x,self.size_y)
        container = QWidget()

        self.main_layout = QVBoxLayout(container)
        self.main_layout.setContentsMargins(50,50,50,50)

        self.main_layout.addStretch()

        self.grid = QGridLayout()
        self.grid.setVerticalSpacing(30)
        self.grid.setHorizontalSpacing(100)
        self.main_layout.addLayout(self.grid)

        self.name_label = QLabel("Enter your full name",self)

        self.input_field = QLineEdit()
        self.input_field.setFixedHeight(36)
        self.input_field.setText("Mam Sayo")#default text?

        self.copy_field = QLineEdit()
        self.copy_field.setReadOnly(True)
        self.copy_field.setFixedHeight(36)
        self.copy_field.setText("Mam Sayo")#I guess this too?

        self.copy_btn = QPushButton("Click to display your fullname")
        self.copy_btn.clicked.connect(lambda: self.copy_field.setText(self.input_field.text()))

        self.grid.addWidget(self.name_label,0,0)
        self.grid.addWidget(self.input_field,0,1)
        self.grid.addWidget(self.copy_btn,1,0)
        self.grid.addWidget(self.copy_field,1,1)

        self.main_layout.addStretch()

        self.setCentralWidget(container)
        
        self.setStyleSheet("""
            QLabel{
                color:red;
            }
            QPushButton{
                color:red;
            }
        """)

        self.show()



app = QApplication(sys.argv)
ex = NameApp()
sys.exit(app.exec())