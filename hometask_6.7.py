tag = input("")
tag_1 = tag.find("<")
tag_2 = tag.find(">")
tag_3 = tag.find("/")
tag_4 = tag.replace(f"{tag[tag_1:tag_2 + tag_3 + 1]}", "")
print(tag_4)

