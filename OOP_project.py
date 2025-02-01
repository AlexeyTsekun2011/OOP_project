import time
import random


# Класс отвечающий за создание поля
class Field:
    def __init__(self, size):
        self.size = size
        self.tiger = Tiger()
        self.bunnies = [Bunny(), Bunny()]  # два bunny в списке т.к. по условию их два

    def draw(self):
        for y in range(self.size):
            for x in range(self.size):
                if self.tiger.coords == [x, y]:  # запись координат  в формате списка
                    print("T ", end="")  # условие на демонстрацию тигра(Т) на игровом поле
                elif any(bunny.coords == (x, y) and bunny.alive for bunny in self.bunnies):
                    print("3 ", end='')  # дополнительное условие  на демонстрацию зайца(З) на игровом поле

                else:
                    print(". ", end="")
            print()

    # Метод отвечающий за обновление состояния тигра исходя из ситуации
    def update(self):
        self.tiger.update_state(self.bunnies)


class Bunny:
    def __init__(self):
        placed = False
        # цикл отвечающий за случайное появления зайца
        while not placed:
            self.coords = (random.randint(0, 4)), random.randint(0, 4)
            # это условие необходимо по заданию т.к. зайцы не должны появляться на месте тигра
            if self.coords != (0, 0):
                placed = True
        self.alive = True


class Tiger:
    def __init__(self):
        self.coords = [0, 0]  # по условию координаты тигра всегда должны быть 0,0
        self.state = "Выследить добычу"
        self.bunny = None

    def update_state(self, bunnies: list[Bunny]):  # метод, переводящий
        if self.state == "Выследить добычу":
            self.seek_bunnies(bunnies)
        elif self.state == "Атаковать добычу":
            self.attack_bunnies()
        elif self.state == "Бежать домой":
            self.go_home()

    def seek_bunnies(self, bunnies: list[Bunny]):
        self.coords[0] += (random.randint(-1, 1))

        if self.coords[0] < 0:  # постановка границ поля №1
            self.coords[0] = 0

        if self.coords[0] > 4:  # постановка границ поля №2
            self.coords[0] = 4

        self.coords[1] += (random.randint(-1, 1))

        if self.coords[1] < 0:  # постановка границ поля №3
            self.coords[1] = 0

        if self.coords[1] > 4:  # постановка границ поля №4
            self.coords[1] = 4
        for bunny in bunnies:
            if abs(self.coords[0] - bunny.coords[0]) <= 1 and abs(self.coords[1] - bunny.coords[1]) <= 1:
                self.state = "Атаковать добычу"
                self.bunny = bunny
                break

    def attack_bunnies(self):
        if random.randint(0, 1):
            self.bunny.alive = False
            print("Успешная атака")
            self.state = "Бежать домой"
        else:
            print("Неуспешная атака")
            self.state = "Выследить добычу"

    def go_home(self):  # состояние волка,
        # которое отвечает за телепортацию домой после поимки зайца
        self.coords[0] = 0
        self.coords[1] = 0


if __name__ == "__main__":
    field = Field(5)  # Величина поля, в аргументе число которое будет в обеих осях
    field.draw()
    print("Начало симуляции")
    while True:
        field.update()  # обновления поля игры из-за постоянного перемещения зайца
        field.draw()
        time.sleep(1)  # таймер после которого происходит движение волка в аргументе кол-во секунд до нового хода
        print("Ход сделан")
        print(field.tiger.state)  # вывод состояния тигра
        if field.tiger.state == "Бежать домой":
            break

    field.update()
    field.draw()
