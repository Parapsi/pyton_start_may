width = int(input("insert width: "))
height = int(input("insert height: "))
def rectangle(x, y):
    global width
    global height
    res = f"{'*' * x}\n" + (f"*{' ' * (x - 2)}*\n") * (y - 2) + f"{'*' * x}"
    return print(res)
rectangle(width, height)