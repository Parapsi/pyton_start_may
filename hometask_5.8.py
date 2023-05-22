import random
lst_1 = [random.randint(1, 10) for i in range(4)]
lst_2 = []
for i in range(len(lst_1)):
        lst_2.append(lst_1[i] * 2)
print(lst_1 + lst_2)
