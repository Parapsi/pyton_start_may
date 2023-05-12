a = int(input("сторона A "))
b = int(input("сторона B "))
c = int(input("сторона C "))
if a + b < c or a + c < b or c + b < a:
    print("такой треугоник не существует")
else:
    print("такой треугольник существует")