class WrongPrice(Exception):
    def __init__(self, price):
        super().__init__()
        self.price = price

    def __str__(self):
        return "Wrong price exception"


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        if self.price <= 0:
            raise WrongPrice(self.price)
        return f"Product name:{self.name}, price:{self.price}, description:{self.description}"


try:
    b = Product("Vodka", -2, "very strong drink")
    print(b)
except WrongPrice as err:
    print(err)
