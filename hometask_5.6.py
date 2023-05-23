FIVE = 5
while True:
    number = int(input("введите число "))
    print(f"{number} x {FIVE} = ", number * FIVE)
    print("хотите продолжить? (yes/no)")
    answer = input()
    if answer == "yes":
        break