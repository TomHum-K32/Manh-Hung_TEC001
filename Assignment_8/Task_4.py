import random

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed = self.speed + change

        if self.speed > self.max_speed:
            self.speed = self.max_speed
        if self.speed < 0:
            self.speed = 0

    def drive(self, hours):
        self.distance = self.distance + self.speed * hours


class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.km = km
        self.cars = cars

    def hour_passes(self):
        i = 0
        while i < len(self.cars):
            change = random.randint(-10, 15)
            self.cars[i].accelerate(change)
            self.cars[i].drive(1)
            i = i + 1

    def print_status(self):
        print("Status: ")
        print("Reg  Speed  Distance")

        i = 0
        while i < len(self.cars):
            c = self.cars[i]
            print(c.reg, c.speed, c.distance)
            i = i + 1

        print("")

    def race_finished(self):
        i = 0
        while i < len(self.cars):
            if self.cars[i].distance >= self.km:
                return True
            i = i + 1
        return False



cars = []

i = 1
while i <= 10:
    reg = "ABC-" + str(i)
    max_speed = random.randint(100, 200)
    car = Car(reg, max_speed)
    cars.append(car)
    i = i + 1

race = Race("Grand Demolition Derby", 8000, cars)

hours = 0

while race.race_finished() == False:
    race.hour_passes()
    hours = hours + 1

    if hours % 10 == 0:
        race.print_status()

race.print_status()
print("Race finished in", hours, "hours")