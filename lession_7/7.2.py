day = int(input("Введите какой сегодня день? "))

try:
    if day > 31:
        raise ValueError("Не бывает такого номера дня")
except ValueError as msg:
    print('Ошибка:', msg)
finally:
    print('Have a nice day')