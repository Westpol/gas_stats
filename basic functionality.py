import json
import datetime
import random
import time
import keyboard


class Menu:

    def __init__(self):
        self._menupoints = [1, 0, 0]

    def refresh(self):
        for i in range(40):
            print()
        self._print_menu(self._menupoints)

    def _print_menu(self, menpoints):
        if keyboard.is_pressed("enter"):
            while keyboard.is_pressed("enter"):
                time.sleep(0.01)
            menpoints[1] = 1
        if menpoints[0] == 1 and menpoints[1] == 0:
            if keyboard.is_pressed("down"):
                while keyboard.is_pressed("down"):
                    time.sleep(0.01)
                self._menupoints[0] += 1
            print("Show data  <")
            print("Add data")
            print("Reset data")
        elif menpoints[0] == 2 and menpoints[1] == 0:
            if keyboard.is_pressed("up"):
                while keyboard.is_pressed("up"):
                    time.sleep(0.01)
                self._menupoints[0] -= 1
            elif keyboard.is_pressed("down"):
                while keyboard.is_pressed("down"):
                    time.sleep(0.01)
                self._menupoints[0] += 1
            print("Show data")
            print("Add data  <")
            print("Reset data")
        elif menpoints[0] == 3 and menpoints[1] == 0:
            if keyboard.is_pressed("up"):
                while keyboard.is_pressed("up"):
                    time.sleep(0.01)
                self._menupoints[0] -= 1
            print("Show data")
            print("Add data")
            print("Reset data  <")

        elif menpoints[0] == 1 and menpoints[1] != 0:
            self._print_dates()

    def _print_dates(self):
        datess = data.get_dates()

        if keyboard.is_pressed("up"):
            while keyboard.is_pressed("up"):
                time.sleep(0.01)
            if 1 < self._menupoints[1] <= len(dates) + 1:
                self._menupoints[1] -= 1

        if keyboard.is_pressed("down"):
            while keyboard.is_pressed("down"):
                time.sleep(0.01)
            if 1 <= self._menupoints[1] < len(dates):
                self._menupoints[1] += 1

        for i in range(len(dates)):
            if i == self._menupoints[1] - 1:
                print(datess[i] + "  <")
            else:
                print(datess[i])


class Data:
    def __init__(self):
        self._dates = []
        self._liters = []
        self._tachometer = []
        self._dt = json.load(open("data.json"))

    def get_dates(self):
        date_list = []
        for i in range(len(self._dt)):
            date_list.append(self._dt[i]["date"])
        return date_list

    def get_data(self, index, typ):
        return self._dt[index][typ]


if __name__ == "__main__":
    data = Data()
    dates = data.get_dates()
    menu = Menu()
    while 1:
        menu.refresh()
        time.sleep(.05)
        if random.randint(0, 5000) == 1:
            break
    print(str(data.get_data(0, "putin")) + " l")
    print(str(round((data.get_data(1, "tachom") - data.get_data(0, "tachom")) / data.get_data(1, "putin"), 2)) + " l/100km")
    print(datetime.date.today().strftime("%d.%m.%Y"))
