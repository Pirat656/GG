import random


class Cat:

    def __init__(self, cat, ):
        self.cat = cat
        self.eat = 0
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print("Time eat")
        self.gladness += 1.25

    def to_study(self):
        print("Time to play")
        self.gladness += 3

    def to_sleep(self):
        print("Time to sleep")
        self.gladness += 3

    def to_chill(self):
        print("Time to rest")
        self.gladness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < 0.5:
            print("Play more")
            self.alive = True
        elif self.gladness <= 0:
            print("Go play")
            self.alive = True
        elif self.progress > 5:
            print("Just live")
            self.alive = True

    def end_of_day(self):
        print(f"Gladness - {self.gladness}")
        print(f"Progress - {round(self.progress, 2)}")

    def life(self, day):
        day = "Day " + str(day + 1) + " of " + self.cat + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_eat()
        elif live_cube == 3:
            self.to_chill()
        self.to_sleep()
        self.end_of_day()
        self.is_alive()


cat = Cat(cat="Tima")

for day in range(365):
    if not cat.alive:
        break
    cat.life(day)
