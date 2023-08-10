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

    def __init__(self):
        self.products = []
        self.result = []
        self.index = 0

    def add_product(self, buyer_name, product, amount, price):
        self.buyer_name = buyer_name
        self.products.append(product)
        self.result.append(amount*price)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return f"{self.products[self.index - 1]}"
        raise StopIteration

    def __str__(self):
        x = ",".join(self.products)
        return f"{self.buyer_name} bought:{x} and spent {sum(self.result)} dollars"


a = Cart()
a.add_product("Alex", "Cucumber", 3, 5)
a.add_product("Alex", "Vodka", 1, 15)
a.add_product("Alex", "Tomato", 2, 3)

print(a)


print(f"{a.buyer_name} bought:\n***********")
for i in a:
    print(i)
print(f"***********\nAnd spent: {sum(a.result)} dollars")
