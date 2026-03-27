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
            print("Wrong floor")
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


e = Elevator(1, 10)

e.go_to_floor(5)

e.go_to_floor(1)