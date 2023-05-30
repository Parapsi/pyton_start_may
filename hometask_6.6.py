word = input("")
x = 1
while len(word[0:x]) // 2 * word.count(word[0:x]) != len(word) // 2:
    x += 1
print(word[0:x])

