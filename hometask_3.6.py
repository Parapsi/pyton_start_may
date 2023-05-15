print("введите число")
number = int(input())
number_1 = (number > 0 and number % 2 == 0 and "число положительное и парное") or "число не отвечает критериям"
print(number_1)