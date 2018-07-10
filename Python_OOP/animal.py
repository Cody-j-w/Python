class Animal:
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print(f"the creature currently has {self.health} health")
        return self
class Dog(Animal):
    def __init__(self,name):
        super().__init__(self)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self,name):
        super().__init__(self)
        self.health = 710
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        print(f"I am a dragon! I have {self.health} health!")
        return self


cat = Animal("Bubb")

cat.walk()
cat.walk()
cat.walk()
cat.run()
cat.run()
cat.display_health()

pupper = Dog("Pupp")

pupper.walk()
pupper.walk()
pupper.walk()
pupper.run()
pupper.run()
pupper.pet()
pupper.display_health()

Drago = Dragon("Seath")

Drago.fly()
Drago.fly()
Drago.display_health()