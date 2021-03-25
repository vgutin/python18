def cat_finder(file_path):
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
