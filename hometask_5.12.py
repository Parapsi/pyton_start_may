lst = []
for i in range(2, 100):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
