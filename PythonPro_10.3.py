import re


def email(text):
    match = re.fullmatch(r'[a-zA-Z0-9]+[-_]?[a-zA-Z0-9]+@[a-z]+.com', text)
    if match:
        return print(True)
    else:
        return print(False)


email("12123sfsdfsd-f@gmail.com")
email("_asdasdqwe@gmail.com")
email("asdasd2231__qweqwe@gmail.com")