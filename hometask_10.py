names = open("hw_10_test.txt", "r+")
lst = []
purchases = {}
spending = {}
names_1 = names.readlines()
member = input("insert family member: \n")
for row in names_1:
    row_1 = row.replace("\n", "").replace("$", "")
    lst.append(row_1)


def action(dictions, objects):
    if dictions.get(objects, False) is False:
        dictions[objects] = [money]
    else:
        dictions[objects].append(money)


for i in lst:
    res = i.split()
    _, *names, money, items = res
    money = float(money)
    names = " ".join(names)
    action(purchases, items)
    action(spending, names)

member_spendings = len(spending[member])
print(f"{member} bought {member_spendings} items and spent {round(sum(spending[member]), 2)} dollars ")
print("-" * 30)


def listed(dictions):
    for j in dictions:
        dictions[j] = sum(dictions[j])
        print(f"{j}: {round(dictions[j], 2)} dollars")


listed(purchases)
print("-" * 30)
listed(spending)
