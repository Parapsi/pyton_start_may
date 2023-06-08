def line(*args):
    summa = 0
    word = ""
    for i in args:
        if type(i) == int:
            summa += i
        elif type(i) == str:
            word = i
    summa_1 = str(summa)
    return summa_1 + word


print(line(22, 22, "Kyiv"))
