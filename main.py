import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QPushButton
import random

if __name__ == "__main__":
    # 2. Create an instance of QApplication
    app = QApplication([])

    # 3. Create your application's GUI
    window = QWidget()
    window.setWindowTitle("PyQt App")
    window.setGeometry(100, 100, 1000, 562)
    helloMsg = QLabel("<h1>Hello, World!{0}</h1>".format(random.randint(0, 9)), parent=window)
    helloMsg.move(60, 15)
    fillBox = QComboBox(parent=window)
    fillBox.addItems(["one", "two", "three"])
    fillBox.move(100, 100)

    # 4. Show your application's GUI
    window.show()

    # 5. Run your application's event loop
    sys.exit(app.exec())
