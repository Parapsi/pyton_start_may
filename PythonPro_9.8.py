class Balance:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    def __str__(self):
        return f"{self.name} balance is: {self.__balance}"

    def __getattr__(self, item):
        print("not exist")


    @property
    def balance(self):
        return print(self.__balance)

    @balance.setter
    def balance(self, value):
        print("cant change balance")


a = Balance("Alex", 25000)
a.balance = 1000
a.balance
a.value
