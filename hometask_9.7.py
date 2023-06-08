numbers = input("insert numbers:")


def value(lst):
    lst = [int(x) for x in numbers.replace(",", " ").split()]
    if lst[3] - lst[2] == lst[1] - lst[0]:
        summ = lst[3] - lst[2]
        lst.append(lst[len(lst)-1] + summ)
        return print(lst)
    elif lst[3] / lst[2] == lst[1] / lst[0]:
        summ = lst[3] / lst[2]
        lst.append(int(lst[len(lst) - 1] * summ))
        return print(lst)
    elif lst[1] ** (1/2) == 2:
        summ = int(lst[len(lst) - 1] ** (1/2) + 1)
        lst.append(summ ** 2)
        return print(lst)
    elif lst[1] ** (1/3) == 2:
        summ = int(lst[len(lst) - 1] ** (1/3) + 1)
        lst.append(summ ** 3)
        return print(lst)


value(numbers)
