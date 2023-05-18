number = input("введите число ")
lst = list(map(int, number))
if sum(lst[:3:]) == sum(lst[3:]):
    print("число счастливое")
else:
    print("число несчастливое")