dictionary = {}
while True:
    word = input("Введите слово ")
    translation = input("Введите превод ")
    dictionary[word] = translation
    x = input("хотите продолжить? Y or N?\n").lower()
    if x != "y":
        break
while True:
    word_1 = input("Введите слово, которое хотите перевести \n")
    print(dictionary.get(word_1, "ошибка ввода"))
    y = input("хотите продолжить? Y or N?\n")
    if y == "y":
        continue
    else:
        break
