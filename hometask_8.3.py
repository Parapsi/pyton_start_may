dictionary = {}
lst_1 = []
lst_2 = []
while True:
    act = input("add/quit?\n").lower()
    while act != "quit":
        if act == "add":
            x = input("word ")
            y = input("meaning ")
            dictionary[x] = y
            lst_1.append(y)
            lst_2 = [i for i in lst_1 if lst_1.count(i) > 1]
            break
        else:
            print("error")
            break
    else:
        st_1 = set(lst_1)
        st_2 = set(lst_2)
        print("dictionary:\n", dictionary,"\n", "unique meanings:\n", st_1 - st_2)
        break
