# Task 3
contacts = {}

while (action := input('name or esc:\n').lower()) != 'esc':
    if action == 'name':
        name = input('name:\n').strip()
        friend = input("friend:\n").strip()
        if name not in contacts:
            contacts[name] = list()
        contacts[name].append(friend)
        print(contacts)
        continue


while (action_1 := input("insert first friend or esc:\n").lower()) != "esc":
    action_2 = input("insert second friend:\n")
    x = set(contacts[action_1])
    y = set(contacts[action_2])
    print("mutual friends:\n", x & y)
