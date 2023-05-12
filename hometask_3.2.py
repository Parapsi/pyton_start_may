year = int(input("введите год "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("366 дей в году")
else:
    print("365 дней в году")