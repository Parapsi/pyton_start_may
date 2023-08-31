import re


def login(text):
    match = re.fullmatch(r'[a-zA-Z0-9]{2,}', text)
    if match:
        return print(True)
    else:
        return print(False)


login("vodkapivo123")
login("v")
login("vodkapivo123_1")