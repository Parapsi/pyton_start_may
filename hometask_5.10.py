a = 0
b = 0
while a <= 20:
    matrix = [a + (i + 1) for i in range(4)]
    print(matrix)
    a += 4
    b += sum(matrix)
print(b)
