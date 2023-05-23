import random
lst_1 = [random.randint(1, 10) for i in range(4)]
print(lst_1)
for i in range(len(lst_1)):
        lst_1.append(lst_1[i] * 2)
print(lst_1)
