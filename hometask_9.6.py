number = int(input("input number"))
symbols = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}


def rome():
    num_1 = number // 1000
    num_2 = number % 1000 // 500
    num_3 = number % 500 // 100
    num_4 = number % 100 // 50
    num_5 = number % 100 // 10
    num_6 = number % 10 // 5
    num_7 = number % 5
    print(f"{symbols[1000] * num_1}{symbols[500] * num_2}{symbols[100] * num_3}{symbols[50] * num_4}{symbols[10] * num_5}{symbols[5] * num_6}{symbols[1] * num_7}")


rome()
