def fibo(stop, start=1):
    number_2 = 1
    index = 1
    while index < stop:
        number_3 = start + number_2
        start = number_2
        number_2 = number_3
        index += 1
        yield number_3


a = fibo(10)
for i in a:
    print(i)

