class Dish:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"{self.name}{self.description}{self.price}"


class MenuCategory:
    def __init__(self):
        self.categories = {}

    def add_dishes(self, name, dish):
        if self.categories.get(name, False) is False:

            self.categories[name] = [[dish.name, dish.price]]
        else:
            self.categories[name].append([dish.name, dish.price])

    def __str__(self):
        res = ""
        for category in self.categories:
            res += f'{category.upper()}:\n'
            for dish in self.categories[category]:
                res += f"{dish[0]}: {dish[1]} dollars\n"

        return res


class DiscountException(Exception):
    def __init__(self, discount):
        super().__init__()
        self.discount = discount

    def __str__(self):
        return "Wrong discount"


class Discount:
    def __init__(self, value=0):
        self.value = value

    def discount(self):
        return 1 - self.value / 100


class RegularDiscount(Discount):
    def __init__(self, value=5):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class SilverDiscount(Discount):
    def __init__(self, value=10):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100


class GoldDiscount(Discount):
    def __init__(self, value=20):
        super().__init__(value)

    def discount(self):
        return 1 - self.value / 100

class Order:
    def __init__(self):
        self.your_order = {}

    def add_item(self, item):
        self.your_order[item.name] = item.price

    def remove_item(self, item):
        del self.your_order[item]

    def calculate_total(self, discount: Discount):
        summ = 0
        for item in self.your_order:
            summ += self.your_order[item]
        res = ''
        for item in self.your_order:
            res += f'{str(item)} '
        if discount.discount() >= 100 or discount.discount() <= 0:
            raise DiscountException(discount.discount())
        return f"Your order: {res}\nTotal is {summ * discount.discount():.2f} dollars"


banana = Dish("banana", "fruit", 23)
apple = Dish("apple", "fruit", 32)
meat = Dish("steak", "meat", 150)
order = MenuCategory()
order.add_dishes("fruits", banana)
order.add_dishes("fruits", apple)
order.add_dishes("steak", meat)
print(order)

e = Order()
e.add_item(banana)
e.add_item(apple)
e.add_item(meat)
e.remove_item("banana")
print(e.calculate_total(GoldDiscount()))
try:
    print(e.calculate_total(Discount(100)))
except DiscountException as err:
    print(err)

