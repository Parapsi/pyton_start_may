names = open("hw_10_test.txt", "r+")
lst = []
purchases = {}
spending = {}
names_1 = names.readlines()
member = input("insert family member: \n")
for row in names_1:
    row_1 = row.replace("\n", "").replace("$", "")
    lst.append(row_1)
for i in lst:
    res = i.split()
    _, *names, money, objects = res
    money = float(money)
    names = " ".join(names)
    if purchases.get(objects, False) is False:
        purchases[objects] = [money]
    elif spending.get(names, False) is False:
        spending[names] = [money]
    else:
        purchases[objects].append(money)
        spending[names].append(money)

member_spendings = len(spending[member])
print(f"{member} bought {member_spendings} items and spent {round(sum(spending[member]), 2)} dollars ")
print("-" * 30)
for i in purchases:
    purchases[i] = sum(purchases[i])
    print(f"{i}: {round(purchases[i], 2)}")
print("-" * 30)
for i in spending:
    spending[i] = sum(spending[i])
    print(f"{i} spent: {round(spending[i], 2)} dollars")
