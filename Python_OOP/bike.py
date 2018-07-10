class Bike:
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
       print(f"costs {self.price}, goes {self.max_speed}, has gone {self.miles} miles.")
    def ride(self):
        print("Wheee!")
        self.miles += 10
        print(f"you had ridden for {self.miles} miles!")
    def reversing(self):
        if self.miles == 0:
            print("Can't back up any further!")
        else:
            print("Backing up! Backing up! Backing up!")
            self.miles -=5