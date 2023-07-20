class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product name:{self.name}, price:{self.price}, description:{self.description}"


b = Product("Vodka", "2$", "very strong drink")
print(b)


class Cart:
    result = []
    products = []

    def __init__(self, buyer_name, product, amount, price):
        self.buyer_name = buyer_name
        self.product = product
        self.amount = amount
        self.price = price
        summa = self.amount * self.price
        Cart.result.append(summa)
        Cart.products.append(self.product)

    def __str__(self):
        x = ",".join(Cart.products)
        return f"{self.buyer_name} bought:{x} and spent {sum(Cart.result)}"


a = Cart("Alex", "vodka", 3, 2.5)
b = Cart("Alex", "cucumber", 5, 1)

print(b)
