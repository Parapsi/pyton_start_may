word = input("")
word_1 = list(word)
word_2 = []
for a in word_1:
    if not a in word_2:
        word_2.append(a)
print(word_2)
