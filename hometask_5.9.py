import random
salary = [random.randint(5000, 10000) for i in range(12)]
print("зарплаты за год ", salary)
print("средняя зарплата ", round((sum(salary) / len(salary))))
