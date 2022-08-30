question = input("Какая у вас зарплата? ")
salary = float(question)
year_salary = salary * 12
tax = 0.1
answer = ("Ваш налог: ")
if year_salary < 9076:
    tax = 0.1
if year_salary >= 9076 and year_salary < 36901:
    tax = 0.15
if year_salary >= 36901 and year_salary < 89351:
    tax = 0.25
if year_salary >= 89351 and year_salary < 186351:
    tax = 0.28
if year_salary >= 186351 and year_salary < 405101:
    tax = 0.33
if year_salary >= 405101 and year_salary < 406751:
    tax = 0.35
if year_salary >= 406751:
    tax = 0.396
result = round(tax * year_salary, 2)
print(answer, str(result))
