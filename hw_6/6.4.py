user_bdate = input('Введите дату рождения: ')
# TODO: добавить обработку для исключения входных данных не являющихся целочисленными значениями

file_path = 'lesson06_pi_million_digits.txt'

with open(file_path) as file:
    count = 0  # счетчик строк
    end = True  # флаг для определения конца файла
    for line in file:
        count += 1
        index = line.find(user_bdate)  # ищем индекс (позицию) первого вхождения в итерируемой строке файла
        if index != -1:
            print(f'Число найдено в строке: {count} позиция в строке: {index}')
            end = False  # число найдено, переключаем флаг
            break
    if end is True:  # если флаг не переключен, значит число не нашли
        print('Не найдено')
    file.close()
