text = input("напечатайте текст \n")
lst = text.replace(",", " ").split()
while len(lst) > 1:
    if len(lst[0]) > len(lst[1]):
        lst.remove(lst[1])
    else:
        lst.remove(lst[0])
print(lst)