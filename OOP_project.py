import random
import time


class Field:
    def __init__(self,size,bunnies):
        self.size = size
        self.grid = []
        for i in range(size):
            self.grid.append([None] * self.size)


class Bunny:
    def __init__(self,size):
        placed = False
        while not placed:
            self.coords =(random.randint(0,4)), random.randint(0,4)
            self.coords[0] += (random.randint(-1, 1))

            if self.coords != (0,0):
                placed = True


class Tiger:
    def __init__(self):
        self.coords = [0,0]
        self.state = "Выследить добычу"

    def countdown(self,name, countdown_time):
        while countdown_time > 0:
            print(f"До нового хода {countdown_time}")
            time.sleep(1)
            countdown_time -= 1
        else:
            print("Время вышло")


    def seek_bunnies(self,walk):
        search = False
        while not search:
            self.coords[0] += (random.randint(-1, 1))

            if self.coords[0] < 0:
                self.coords[0] = 0

            if self.coords[0] > 4:
                self.coords[0] = 4

            self.coords[1] += (random.randint(-1,1))

            if self.coords[1] < 0:
                self.coords[1] = 0

            if self.coords[1] > 4:
                self.coords[1] = 4



    def attack_bunnies(self,attack):
        find = False
        while not find:
            if self.coords[0] or self.coords[1]

    def go_home(self):
        go = False
        while not go:
            if #Заяц был пойман
                self.coords[0] = 0
                self.coords[1] = 0
                #Спросить break или go = True














