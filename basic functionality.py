import json
import datetime
import random
import sys
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

        # -------------------------------------------------------------------------------
        if keyboard.is_pressed("backspace"):
            while keyboard.is_pressed("backspace"):
                time.sleep(0.01)

            if self._menupoints[1] == 0:
                print("Do you want to exit? Backspace to exit, enter to stay in the menu.")
                while 1:
                    if keyboard.is_pressed("backspace"):
                        sys.exit()
                    if keyboard.is_pressed("enter"):
                        while keyboard.is_pressed("enter"):
                            time.sleep(0.01)
                        break
            if self._menupoints[0] != 0:
                if self._menupoints[1] != 0 and self._menupoints[2] == 0:
                    self._menupoints[1] = 0
                if self._menupoints[2] != 0:
                    self._menupoints[2] = 0
        # ---------------------------------------------------------\_ go one step back in menu /‾ go one step further
        # in menu
        if keyboard.is_pressed("enter"):
            while keyboard.is_pressed("enter"):
                time.sleep(0.01)
            if self._menupoints[0] != 0:
                if self._menupoints[1] != 0:
                    self._menupoints[2] = 1
                    menpoints[2] = 1
                else:
                    self._menupoints[1] = 1
                    menpoints[1] = 1
        # ------------------------------------------------------------------------------

        # ------------------------------------------------------------------------------
        if self._menupoints[1] == 0 and self._menupoints[2] == 0:
            if keyboard.is_pressed("up"):
                while keyboard.is_pressed("up"):
                    time.sleep(0.01)
                if 1 < self._menupoints[0]:
                    self._menupoints[0] -= 1
            elif keyboard.is_pressed("down"):
                while keyboard.is_pressed("down"):
                    time.sleep(0.01)
                if self._menupoints[0] < 3:
                    self._menupoints[0] += 1
        # --------------------------------------\_ move up/down in menu when Arrow keys are used  /‾ print menu
            menupoints = ["Show Data", "Add Data", "Reset Data"]
            for i in range(0, 3):
                if i + 1 == menpoints[0]:
                    print(menupoints[i] + "  <")
                else:
                    print(menupoints[i])
        # ------------------------------------------------------------------------------

        # get into lower menus ‾\
        if menpoints[0] == 1 and menpoints[1] != 0 and menpoints[2] == 0:
            self._print_dates()
        if menpoints[0] == 1 and menpoints[1] != 0 and menpoints[2] != 0:
            self._print_stats()

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

    def _print_stats(self):
        dataa = data.dt
        print("tachom: " + str(dataa[self._menupoints[1] - 1]["tachom"]) + " km")
        print("put in: " + str(dataa[self._menupoints[1] - 1]["putin"]) + " l")
        print("price per liter: " + str(dataa[self._menupoints[1] - 1]["ppl"]) + " €/l")
        print("paid: " + str(round(float(dataa[self._menupoints[1] - 1]["ppl"]) * float(dataa[self._menupoints[1] - 1]["putin"]), 2)) + " €")
        if self._menupoints[1] - 2 >= 0:
            print("liters per 100km: " + str(dataa[self._menupoints[1] - 1]["putin"] / ((dataa[self._menupoints[1] - 1]["tachom"] - dataa[self._menupoints[1] - 2]["tachom"]) / 100)) + " l/100km")


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
    print(str(round((data.get_data(1, "tachom") - data.get_data(0, "tachom")) / data.get_data(1, "putin"), 2)) +
          " l/100km")
    print(datetime.date.today().strftime("%d.%m.%Y"))
