bDate = input("В каком году вы родились?")
while True:
    try:
        bDate = int(bDate)
        if bDate < 1:
            bDate = input("Ошибка ввода. Год не может быть равен 0 или отрицательным. Введите корректный год")
        else:
            break
    except ValueError:
        bDate = input("Ошибка ввода. Пожалуйста введите целочисленное значение")

tDate = input("К какому году нужно посчитать возраст?")
while True:
    try:
        tDate = int(tDate)
        if tDate < 1 or tDate < bDate:
            tDate = input("Ошибка ввода. Год не может быть равен 0, отрицательным или меньше года рождения. Введите корректный год")
        else:
            break
    except ValueError:
        tDate = input("Ошибка ввода. Пожалуйста введите целочисленное значение")

result = str(tDate - bDate)
print ("В " + str(tDate) + " году Вам будет " + result + " лет")

