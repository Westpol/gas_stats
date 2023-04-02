import sys
from PyQt6.QtWidgets import *
import json


class Data:
    def __init__(self):
        self._dates = []
        self._liters = []
        self._tachometer = []
        self.dt = json.load(open("data_raw.json"))

    def get_dates(self):
        date_list = []
        for i in range(len(self.dt)):
            date_list.append(self.dt[i]["date"])
        return date_list

    def get_data(self, index, typ):
        return self.dt[index][typ]


class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        self._data = Data()
        self._dates = self._data.get_dates()
        self.setWindowTitle("QTabWidget Example")
        self.resize(1000, 562)
        # Create a top-level layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        # Create the tab widget with two tabs
        tabs = QTabWidget()
        for i in range(len(self._dates)):
            tabs.addTab(self.generalTabUI(i), self._dates[i])
        # tabs.addTab(self.generalTabUI(), "General")
        # tabs.addTab(self.networkTabUI(), "Network")
        layout.addWidget(tabs)

    def generalTabUI(self, num):
        """Create the General page UI."""
        generalTab = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(QCheckBox(str(self._data.dt[num]["date"])))
        layout.addWidget(QCheckBox(str(self._data.dt[num]["tachom"]) + " km"))
        layout.addWidget(QCheckBox(str(self._data.dt[num]["putin"]) + " l"))
        layout.addWidget(QCheckBox(str(self._data.dt[num]["ppl"]) + " €/l"))
        generalTab.setLayout(layout)
        return generalTab


if __name__ == "__main__":
    data = Data()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
