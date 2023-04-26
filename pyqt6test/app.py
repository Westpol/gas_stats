import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWondow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fuck meee pllllls X(")
        button = QPushButton("I neeeed your cum X(")
        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = MainWondow()
window.show()

app.exec()
