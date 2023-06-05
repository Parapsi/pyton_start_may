sentence_1 = input("insert first sentence:\n").replace(",", "").split()
sentence_2 = input("insert second sentence:\n").replace(",", "").split()
lst_1 = []
lst_2 = []
for i in sentence_1:
    if len(i) == len(max(sentence_1, key=len)):
        lst_1.append(i)
for j in sentence_2:
    if len(j) == len(max(sentence_2, key=len)):
        lst_2.append(j)
st_1 = set(lst_1)
st_2 = set(lst_2)
print("longest mutual word: ", st_1 & st_2)
