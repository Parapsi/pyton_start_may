text = input("")
lane = text.replace(",", " ").split()
dict = {}
for i in lane:
    dict[i] = lane.count(i)
print(dict)


