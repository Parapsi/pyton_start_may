def cube(stop, start=2):
    lst = [i ** 3 for i in range(start, stop + 1)]
    yield lst


a = cube(10)
for j in a:
    print(j)
