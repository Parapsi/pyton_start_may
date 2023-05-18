import math
RADIUS = 4
x = float(input("x = "))
y = float(input("y = "))
rad = math.sqrt(x ** 2 + y ** 2)
if math.pi * RADIUS ** 2 >= math.pi * rad ** 2:
    print("точка находится всередине круга")
else:
    print("точка находится за пределами круга")
