class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
        print("Start at", self.current)

    def floor_up(self):
        if self.current < self.top:
            self.current = self.current + 1
            print("Up to", self.current)
        else:
            print("Top")

    def floor_down(self):
        if self.current > self.bottom:
            self.current = self.current - 1
            print("Down to", self.current)
        else:
            print("Bottom")

    def go_to_floor(self, target):
        print("Go to", target)

        if target > self.top or target < self.bottom:
            print("Wrong")
        else:
            if self.current < target:
                while self.current != target:
                    self.floor_up()
            elif self.current > target:
                while self.current != target:
                    self.floor_down()
            else:
                print("Here")

        print("At", self.current)


class Building:
    def __init__(self, bottom, top, num):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        i = 0
        while i < num:
            e = Elevator(bottom, top)
            self.elevators.append(e)
            i = i + 1

    def run_elevator(self, num, target):
        print("Run elevator", num)

        if num < 0 or num >= len(self.elevators):
            print("No elevator")
        else:
            self.elevators[num].go_to_floor(target)


b = Building(1, 10, 3)

b.run_elevator(0, 5)

b.run_elevator(1, 7)

b.run_elevator(0, 1)