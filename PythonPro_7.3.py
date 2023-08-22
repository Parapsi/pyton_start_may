def numbers(stop, start=1):
    for num_1 in range(start, stop + 1):
        for num_2 in range(2, num_1):
            if num_1 % num_2 == 0:
                start += 1
                break
        else:
            yield num_1


b = numbers(211)
for i in b:
    print(i)
