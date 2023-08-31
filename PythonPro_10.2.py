import re


def card(num):
    match = re.fullmatch(r'[0-9]{4}(?:[--][0-9]{4}){3}', num)
    if match:
        return print(True)
    else:
        return print(False)

card("9999-9999-9999-9999")
card("999-0000")