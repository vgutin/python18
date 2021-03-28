family_wage = 0

for i in range(3):
    wage = input("Какая зарплата у " + str(i + 1) + " члена семьи?")
    while True:
        try:
            wage = float(wage)
            if wage < 1:
                wage = input("Ошибка ввода. Зарплата не может быть равна 0 или быть отрицательной.")
            else:
                family_wage = family_wage + wage
                break
        except ValueError:
            wage = input("Ошибка ввода. Пожалуйста числовое значение")

family_wage = family_wage / 3
print("Среднее число: " + str(family_wage))
