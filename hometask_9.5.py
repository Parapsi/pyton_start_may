numbers = float(input("insert money: "))
numbers_1 = numbers * 100
words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve'}


def translation():
    number_1 = numbers_1 // 10000
    number_2 = numbers_1 // 1000 % 10
    number_3 = numbers_1 // 100 % 10
    number_4 = numbers_1 // 10 % 10
    number_5 = numbers_1 % 10
    return print(f"{words[number_1]} hundred {words[number_2]}ty {words[number_3]} dollars {words[number_4]} {words[number_5]} cents")


translation()
