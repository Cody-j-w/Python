class Product:
    def __init__(self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "For sale"
    def sell(self):
        self.status = "Sold"
        return self
    def addTax(self, tax):
        self.price += (self.price*tax)
        return self.price
    def returnItem(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "Defective"
            self.price = 0
        if reason_for_return == "like_new":
            self.status = "For sale"
        if reason_for_return == "opened":
            self.status = "Used"
            self.price *= 0.80
        return self
    def display_info(self):
        print('*'*40)
        print(f"information for: {self.item_name}")
        print(f"price: {self.price}")
        print(f"weight: {self.weight}")
        print(f"brand:{self.brand}")
        print(f"sale status: {self.status}")
        print('*'*40)
        return self

tomato = Product(2, "tomato", "4 ounces", "dole")

tomato.returnItem('opened')
tomato.display_info()
