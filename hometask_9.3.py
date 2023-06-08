def search():
    numbers = input("insert numbers:\n")
    number = input("insert search number:\n")
    numbers = numbers.replace(",", " ").split()
    for i in numbers:
        if i == number:
            number = numbers.index(i)
            return number
    else:
        return -1


print(search())
