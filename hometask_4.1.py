number = int(input("введите число "))
strng = str(number)
lucky = list(map(int, strng))
if len(lucky) == 6 and lucky[0] + lucky[1] + lucky[2] == lucky[3] + lucky[4] + lucky[5]:
    print("число счастливое")
else:
    print("число несчастливое")
