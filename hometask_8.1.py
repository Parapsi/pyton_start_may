while (text := input("введите список\n")) != "":
    lst = text.split()
    setup = set(lst)
    if len(lst) != len(setup):
        print("значения не уникальны")
    else:
        print("значения уникальны")
