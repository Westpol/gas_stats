from matplotlib import pyplot as plt
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


def lp100km(xi):
    if xi >= 1:
        return data.get_data(xi, "putin") / ((data.get_data(xi, "tachom") - data.get_data(xi - 1, "tachom")) / 100)
    return 6.8


if __name__ == "__main__":
    data = Data()

    tachoms = []
    indexes = []

    for i in range(0, len(data.get_dates())):
        indexes.append(i)
        tachoms.append(lp100km(i))

    plt.plot(indexes, tachoms, color="red")

    plt.show()
