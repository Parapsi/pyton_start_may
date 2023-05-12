import math
flat_number = int(input("номер квартиры "))
if flat_number <= 0 or flat_number > 144:
    print("неправильный номер квартиры")
else:
    print("подьезд номер ", math.ceil(flat_number / 36))
    print("этаж номер ", math.ceil((flat_number % 36) / 4) or math.ceil((flat_number % 36) / 4) + 9)
    print(f"квартира номер {flat_number % 4 or (flat_number % 4) + 4} на этаже")
