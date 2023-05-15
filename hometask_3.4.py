print("у вас есть права?")
license = input()
permition = (len(license) == 2 and "не") or ""
print(f"вы {permition} можете водить автомобиль")
