class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        def display_all(self):
            print(f"price: {self.price}")
            print(f"speed: {self.speed}")
            print(f"fuel: {self.fuel}")
            print(f"mileage: {self.mileage}")
            print(f"tax: {self.tax}")
            print('*'*50)
            return self
        display_all(self)



car1 = Car(20000, "90mph", "full", "40mpg")
car2 = Car(500, "20mph", "near-empty", "5mpg")
car3 = Car(5000, "65mph", "half-full", "30mpg")
car4 = Car(50, "2mph", "always full", "doesn't use fuel")
car5 = Car(100000, "200mph", "half-empty", "uses up tires quicker than fuel")
car6 = Car(1000, "80mph", "full", "25mph")
car1.display_all()
