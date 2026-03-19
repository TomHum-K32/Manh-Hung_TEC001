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
    
    def drive(self, hours):
        self.travelled_dis += self.current_speed * hours
    
car = Car("ABC-123", 142)
car.accelerate(60)
car.drive(1.5)

print("Current speed:", car.current_speed, "km/h")
print("Travelled distance:", car.travelled_dis, "km")
