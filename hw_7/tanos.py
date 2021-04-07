import random
import os


def make_random_files():
    count_files = random.randint(5, 15)  # определяем случайное количество создаваемых файлов
    for i in range(1, count_files):
        file_name = str(random.randint(1000000, 9999999)) + '.txt'  # даем случайное 7 значное имя файла
        file = open(file_name, 'w')
        file.close()
        print(f'Создан файл: {file_name}')


def delete_random_files():
    files = os.listdir()
    max_delete = int(len(files) / 2)
    files_deleted = 0  # флаг для определения количества удаленных файлов
    random.shuffle(files)  # перемешиваем список файлов для случаного удаления
    for file in files:
        this_script = os.path.split(__file__)[1]  # имя текущего скрипта для исклчюения из списка удаляемых файлов
        if file != this_script and max_delete > files_deleted:
            os.remove(file)
            print(f'Удален файл: {file}')
            files_deleted += 1
    if files_deleted == 0:
        print('Нечего удалять')


def run(error=0):
    if error == -1:
        action = str(input('Ошибка ввода\n'
                           'Выберете действие (Сгенерировать/Удалить/Мне повезет): ')).strip().lower()
    else:
        action = str(input('Добро пожаловать! Данная программа позволяет в текущей директории сгенерировать случайное '
                           'количество файлов, либо удалить половину\n'
                           'Выберете действие (Сгенерировать/Удалить/Мне повезет): ')).strip().lower()
    if action == 'сгенерировать':
        make_random_files()
    elif action == 'удалить':
        delete_random_files()
    elif action == 'мне повезет':
        luck = random.randint(1, 2)  # шанс любого исхода 50 на 50
        if luck == 1:
            make_random_files()
        else:
            delete_random_files()
    else:
        run(-1)


run()
