def cat_finder(file_path):
    """
        Поиск слова "кошка" в тексте\n
        Функция принимает путь к текстовому файлу,
        считывает его и выводит на экран:\n
        - строку целиком, содержащую слово "кошка"
        - количество упоминаний слово "кошка"


        Parameters
        ----------
        file_path : str
    """
    with open(file_path) as file:
        count_cat = 0
        for line in file:
            cat_index = line.find('кошка ')
            if cat_index != -1:
                print(line.rstrip())
                split_str = line.split()
                for word in split_str:
                    if word == 'кошка':
                        count_cat += 1
        file.close()
        print(f'Количество упоминаний слова "кошка" в тексте: {count_cat}')


path = 'lesson06_cats_of_ulthar.txt'
cat_finder(path)
