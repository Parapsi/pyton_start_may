number = input("введите число ")
lst = list(map(int, number))
lenght = len(lst)//2
if sum(lst[:lenght:]) == sum(lst[lenght:]):
    print("число счастливое")
else:
    print("число несчастливое")