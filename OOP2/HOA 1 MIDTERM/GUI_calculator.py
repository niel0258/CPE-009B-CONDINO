import math
import sys
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QWidget,
    QSizePolicy
)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("pythonico.ico"))

        self.init_menu_bar()
        self.init_ui()

        self.setGeometry(300, 300, 320, 220)
        self.show()

    def init_menu_bar(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")

        exitButton = QAction("Exit", self)
        exitButton.setShortcut("Ctrl+Q")
        exitButton.setStatusTip("Exit application")
        exitButton.triggered.connect(self.close)
        file_menu.addAction(exitButton)

        edit_menu = menu_bar.addMenu("Edit")

        clear_action = QAction("Clear", self)
        clear_action.setShortcut("Ctrl+C")
        clear_action.triggered.connect(self.clear_display)
        edit_menu.addAction(clear_action)

    def init_ui(self):
        container = QWidget()
        self.setCentralWidget(container)

        grid = QGridLayout()
        container.setLayout(grid)

        self.text_line = QLineEdit(self)
        grid.addWidget(self.text_line, 0, 0, 1, 5)#what row and column, then the span

        buttons = [
            '^','sin','cos','(',')',
            '7','8','9','/','*',
            '4','5','6','+','-',
            '1','2','3','C','=',

        ]

        positions = [(r, c) for r in range(1, 6) for c in range(5)]

        for position, name in zip(positions, buttons):
            button = QPushButton(name)
            grid.addWidget(button, *position)
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            button.clicked.connect(
                lambda checked, text=name: self.eval_btn(text)
            )

    def clear_display(self):
        self.text_line.clear()

    def eval_btn(self, char):
        current_text = self.text_line.text()

        if char == "C":
            self.clear_display()

        elif char == "=":
            if not current_text or current_text == "Error":
                return

            try:
                expression = current_text.replace("^", "**")

                # Auto-close unclosed parenthesis (e.g., 'sin(90' -> 'sin(90)')
                open_pars = expression.count("(")
                close_pars = expression.count(")")
                if open_pars > close_pars:
                    expression += ")" * (open_pars - close_pars)

                # Wrap sin(...) and cos(...) inputs with math.radians()
                expression = expression.replace("sin(", "math.sin(math.radians(")
                expression = expression.replace("cos(", "math.cos(math.radians(")

                # Add extra closing parenthesis for the math.radians wrapper
                if "math.radians(" in expression:
                    expression = expression.replace(")", "))")

                result = eval(expression, {"math": math}) #evaluates the string,treats it like  a number. returns a float
                
                # Format to remove tiny floating point inaccuracies (e.g., sin(180) -> 0 instead of 1.22e-16)
                result = round(result, 10)
                
                # Convert whole numbers like 1.0 to 1
                if result.is_integer():
                    result = int(result)

                self.store_ans(str(result))
                self.text_line.setText(str(result))
                
            except Exception:
                self.text_line.setText("Error")

        else:
            if current_text == "Error":
                current_text = ""

            if char in ["sin", "cos"]:
                self.text_line.setText(current_text + char + "(")
            else:
                self.text_line.setText(current_text + char)

    def store_ans(self,data) :
        with open("answer_history.txt",mode='w',encoding='utf-8') as file:
            file.write(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec())