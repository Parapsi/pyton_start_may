text = input("")
lane = text.replace(",", " ").split()
dictionary = {}
for i in lane:
    dictionary[i] = lane.count(i)
print(dictionary)


