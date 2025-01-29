import random
import time


class Field:
    def __init__(self, size):
        self.size = size
        self.grid = []
        for i in range(size):
            self.grid.append([None] * self.size)



class Bunny:
    def __init__(self, size):
        placed = False
        while not placed:
            self.coords = (random.randint(0, 4)), random.randint(0, 4)

            if self.coords != (0, 0):
                placed = True
        self.alive = True


class Tiger:
    def __init__(self):
        self.coords = [0, 0]
        self.state = "Выследить добычу"
        self.bunny = None

    def countdown(self, countdown_time):
        while countdown_time > 0:
            print(f"До нового хода {countdown_time}")
            time.sleep(1)
            countdown_time -= 1
        else:
            print("Ход завершён")

    def update_state(self, bunnies: list[Bunny]):
        if self.state == "Выследить добычу":
            self.seek_bunnies(bunnies)
        elif self.state == "Атаковать добычу":
            self.attack_bunnies(self.bunny)
        elif self.state == "Бежать домой":
            self.go_home()

    def seek_bunnies(self, bunnies: list[Bunny]):
        self.coords[0] += (random.randint(-1, 1))

        if self.coords[0] < 0:
            self.coords[0] = 0

        if self.coords[0] > 4:
            self.coords[0] = 4

        self.coords[1] += (random.randint(-1, 1))

        if self.coords[1] < 0:
            self.coords[1] = 0

        if self.coords[1] > 4:
            self.coords[1] = 4
        for bunny in bunnies:
            if abs(self.coords[0] - bunny.coords[0]) <= 0 and abs(self.coords[1] - bunny.coords[1]) <= 0:
                self.state = "Атаковать добычу"
                self.bunny = bunny
                break

    def attack_bunnies(self, bunny):
        if random.randint(0, 1):
            self.bunny.alive = False
            self.state = "Бежать домой"
        else:
            self.state = "Выследить добычу"

    def go_home(self):
        self.coords[0] = 0
        self.coords[1] = 0
