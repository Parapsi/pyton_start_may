def prog(num, factor):
    start = 1
    while start <= num:
        yield start ** factor
        start += 1
    return


b = prog(10, 2)
for i in b:
    print(i)