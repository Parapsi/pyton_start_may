def rng(start=0, stop=0, step=1):
    while start < stop:
        yield start + step
        start += 1


b = rng(0, 10)
for i in b:
    print(i)