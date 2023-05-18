number = int(input("введите число "))
strng = str(number)
palindrome = list(map(int, strng))
if len(palindrome) % 2 == 0 and palindrome[::-1] == palindrome[:]:
    print("число является палиндромом")
else:
    print("число не является палиндромом")
