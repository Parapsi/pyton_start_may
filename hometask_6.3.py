word = input("ведите слово ")
lane = list(word)
summ = 0
for i in lane:
    summ += ord(i)
print(summ)
