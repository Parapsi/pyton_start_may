number = 0
SEVEN = 7
while True:
    if number % SEVEN == 0 and number < 100:
        print(number)
        number += SEVEN
    else:
        number += SEVEN
