import random
# import os


def make_random_files():
    count_files = random.randint(5, 15)
    random_files = ''
    for i in range(1, count_files):
        file_name = str(random.randint(1000000, 9999999)) + '.txt'
        file = open(file_name, 'w')
        file.close()
        random_files += file_name + '\r'

        print(random_files)


def run(error=0):
    if error == -1:
        action = str(input('Ошибка ввода\n'
                           'Выберете действие (Сгенерировать/Удалить/Мне повезет): ')).strip().lower()
    else:
        action = str(input('Добро пожаловать! Это программа подразумевалась как '
                           'клон https://thanosjs.org/ написанный на Python,\n'
                           'но так как автор ленив до ручного создания файлов,'
                           'а проверять на рабочих файлах является безумием,\n'
                           'то был добавлен генератор случайного количества файлов '
                           'со случайным названием. Больше случайностей богу случайностей!\n'
                           'Данная программа позволяет в текущей директории сгенерировать случайное '
                           'количество файлов, либо удалить половину\n'
                           'Выберете действие (Сгенерировать/Удалить/Мне повезет): ')).strip().lower()
    if action == 'сгенерировать':
        make_random_files()
    elif action == 'удалить':
        pass
    elif action == 'мне повезет':
        pass
    else:
        run(-1)


run()
