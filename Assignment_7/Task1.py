class Car:
    def __init__(self, reg_number, max_speed):
        self.reg_number = reg_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_dis = 0


car = Car("ABC-123", 142)

print("Registration number:", car.reg_number)
print("Maximum speed:", car.max_speed, "km/h")
print("Current speed:", car.current_speed, "km/h")
print("Travelled distance:", car.travelled_dis, "km")