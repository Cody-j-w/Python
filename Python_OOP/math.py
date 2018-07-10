class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, val, *vals):
        self.result += val
        for i in vals:
            self.result += i
        return self
    def subtract(self, val, *vals):
        self.result -= val
        for i in vals:
            self.result -= i
        return self




md = MathDojo()

x = md.add(2).add(2,5,1).subtract(3,2).result

print(x)