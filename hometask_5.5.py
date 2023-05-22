x = int(input("введите длинну "))
y = int(input("введите ширину "))
z = 1
while z <= x or z <= y:
    if z == 1:
        print("*" * x)
    elif z < y:
        print("*", " " * (x - 2), "*")
    elif z == y:
        print("*" * x)
    z += 1
