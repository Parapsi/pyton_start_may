dictionary = {}
while True:
    action = input("введите действие: добавить, вывести, удалить или выйти\n")
    while action != "выйти":
        if action == "добавить":
            name = input("Введите имя ")
            number = input("Введите номер телефона ")
            dictionary[name] = number
            break
        elif action == "вывести":
            name_1 = input("Введите имя для поиска \n")
            print(dictionary.get(name_1, "ошибка ввода"))
            break
        elif action == "удалить":
            print("Введите имя контакта")
            delete = input()
            del dictionary[delete]
            break
        elif action == "выйти":
            break
        else:
            print("Ошибка ввода")
