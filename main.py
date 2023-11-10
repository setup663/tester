from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
import sys
import math


def application():
    app = QApplication(sys.argv)
    #главное окно
    window = QMainWindow()
    window.setWindowTitle("приложение")
    window.setGeometry(300, 250, 400, 650)
    window.setFixedSize(400, 650)

    font = QFont()
    font.setPointSize(20)

    xlabel = QLabel(window)
    xlabel.setText("введите x:")
    xlabel.setFont(font)
    xlabel.adjustSize()
    xlabel.move(40, 40)

    alabel = QLabel(window)
    alabel.setText("введите a:")
    alabel.setFont(font)
    alabel.adjustSize()
    alabel.move(40, 120)

    blabel = QLabel(window)
    blabel.setText("введите b:")
    blabel.setFont(font)
    blabel.adjustSize()
    blabel.move(40, 200)

    output = QLabel(window)
    output.setFont(font)
    output.setFixedWidth(400)
    output.move(50, 260)

    xedit = QLineEdit(window)
    xedit.setGeometry(210, 50, 150, 25)

    aedit = QLineEdit(window)
    aedit.setGeometry(210, 130, 150, 25)

    bedit = QLineEdit(window)
    bedit.setGeometry(210, 210, 150, 25)

    btn = QPushButton(window)
    btn.setText("рассчитатать")
    btn.setFont(font)
    btn.setGeometry(90, 330, 240, 65)

    def calculate():
        x = xedit.text()
        a = aedit.text()
        b = bedit.text()
        x = int(x)
        a = int(a)
        b = int(b)
        y = abs(x ** 2 - a ** 2) + ((9 * x) ** 3) / (b - x) ** 3 * math.sin(x/a)
        output.setText(str(y))

    btn.clicked.connect(calculate)








    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()