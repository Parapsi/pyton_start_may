class WrongPrice(Exception):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return "Wrong price exception"


class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        if self.price <= 0:
            raise WrongPrice
    def __str__(self):
        return f"Product name:{self.name}, price:{self.price}, description:{self.description}"


try:
    b = Product("Vodka", 1, "very strong drink")
    print(b)
except WrongPrice as err:
    print(err)
