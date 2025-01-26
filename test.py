import time
def countdown( countdown_time):
    while countdown_time > 0:
        print(f"До нового хода {countdown_time}")
        time.sleep(1)
        countdown_time -= 1
    else:
        print("Время вышло")





countdown(3)
