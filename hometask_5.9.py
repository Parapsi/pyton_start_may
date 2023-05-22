import random
salary = [random.randint(5000, 10000) for i in range(12)]
print("зарплаты за год ", salary)
x = sum(salary)
print("средняя зарплата ", round((x / 12), 2))
