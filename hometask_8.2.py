while (text := input("введите список\n")) != "":
    text_1 = text.replace(",", " ").split()
    quantity = set(text_1)
    text_1 = [i for i in text_1 if text.count(i) > 1]
    quantity_1 = set(text_1)
    print(quantity - quantity_1)


