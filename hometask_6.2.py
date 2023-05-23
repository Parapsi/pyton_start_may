name = input("введите имя \n")
if name.isalpha():
    if name.istitle():
        print("Имя правильное")
    else:
        print("Ошибка ввода")
else:
    print("Ошибка ввода")