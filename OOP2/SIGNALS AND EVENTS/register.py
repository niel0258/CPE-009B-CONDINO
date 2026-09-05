import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, 
    QLineEdit, QLabel, QGridLayout, QVBoxLayout, QHBoxLayout
)
from PyQt6.QtGui import QIcon


class RegisterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Registration Window"
        self.window_width = 300
        self.window_height = 400
        self.row_index = 0
        self.fields = {}
        self.initUI()

    def add_field(self, label_text, is_password=False):
        label = QLabel(label_text, self)
        field = QLineEdit(self)
        field.setFixedHeight(40)
        
        if is_password:
            field.setEchoMode(QLineEdit.EchoMode.Password)

        self.form_grid.addWidget(label, self.row_index, 0)
        self.form_grid.addWidget(field, self.row_index, 1)
        
        self.fields[label_text] = field
        self.row_index += 1

    def initUI(self):
        self.setWindowTitle(self.title)
        
        # Center window on screen
        screen_geo = QApplication.primaryScreen().geometry()
        pos_x = (screen_geo.width() - self.window_width) // 2
        pos_y = (screen_geo.height() - self.window_height) // 2
        self.setGeometry(pos_x, pos_y, self.window_width, self.window_height)
        self.setWindowIcon(QIcon('myicon.ico'))

        # Central widget & Main vertical layout setup
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout(central_widget)
        
        # Form grid layout
        self.form_grid = QGridLayout()
        main_layout.addLayout(self.form_grid)

        # Form fields
        self.add_field("First name:")
        self.add_field("Last name:")
        self.add_field("Username:")
        self.add_field("Password:", is_password=True)
        self.add_field("Email Address:")
        self.add_field("Contact Number:")

        # Add vertical stretch so form fields stay at the top and push buttons down
        main_layout.addStretch()

        # Bottom Button Horizontal Layout
        button_layout = QHBoxLayout()

        self.submit = QPushButton("Submit", self)
        self.submit.setToolTip("Submit and Save")
        #self.submit.clicked.connect(self)
        
        self.clear = QPushButton("Clear", self)
        self.clear.setToolTip("Clear field (this button does nothing... yet)")
        self.clear.clicked.connect( self.clear_all_fields)
        # Place Submit on the left, Clear on the right
        button_layout.addWidget(self.submit)
        button_layout.addStretch()  # Space out the buttons to opposite corners
        button_layout.addWidget(self.clear)

        # Add button bar at the very bottom of the main layout
        main_layout.addLayout(button_layout)

    def submit(self):
        #transfer to csv

            #check each input for any empty string
    
    def clear_all_fields(self):
        for field in self.fields.values():
            field.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegisterApp()
    window.show()
    sys.exit(app.exec())