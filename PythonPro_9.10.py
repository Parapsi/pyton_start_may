class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __str__(self):
        return f'width is {self.__width} and height is {self.__height}'

    def __getattr__(self, item):
        print('not exist')

    @property
    def width(self):
        return print(self.__width)

    @property
    def height(self):
        return print(self.__height)

    @width.setter
    def width(self, value):
        print('cant change width')
        return self.__width

    @height.setter
    def height(self, value):
        print('cant change height')
        return self.__height

    def area(self):
        return print(f'area is {self.__width * self.__height}')


a = Rectangle(12, 25)
a.width = 10
a.height= 12
a.height
a.area()
a.value
print(a)