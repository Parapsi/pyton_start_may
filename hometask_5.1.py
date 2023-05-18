number = 1
SEVEN = 7
while True:
    if number % SEVEN == 0 and number < 100:
        print(number)
        number += 1
    else:
        number += 1
