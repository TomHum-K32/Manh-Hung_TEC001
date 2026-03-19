class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 0

    def accelerate(self, change):
        self.current_speed += change

        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed

        if self.current_speed < 0:
            self.current_speed = 0


car = Car("ABC-123", 142)

car.accelerate(30)
print("Current speed:", car.current_speed, "km/h")

car.accelerate(70)
print("Current speed:", car.current_speed, "km/h")

car.accelerate(50)
print("Current speed:", car.current_speed, "km/h")

car.accelerate(-200)

print("Final speed after emergency brake:", car.current_speed, "km/h")