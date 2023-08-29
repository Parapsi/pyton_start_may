class User:
    def __init__(self, first_name, last_name):
        self.__first_name = first_name
        self.__last_name = last_name

    def __str__(self):
        return f'{self.__first_name}, {self.__last_name}'

    def __getattr__(self, item):

        print('not exist')

    @property
    def first_name(self):
        return print(self.__first_name)

    @property
    def last_name(self):
        return print(self.__last_name)

    @first_name.setter
    def first_name(self, value):
        print('cant change name')
        return self.__first_name

    @last_name.setter
    def last_name(self, value):
        print('cant change last name')
        return self.__last_name

a = User("alex", "grebenyuk")
a.first_name = "petya"
a.last_name = "ivanov"
a.value
a.first_name
a.last_name
print(a)