print("введите число")
number = int(input())
number_1 = (number % 3 == 0 and number % 5 != 0 and "число подходит критериям") or "число не подходит критериям"
print(number_1)