shows = {
    'Секретные материалы': 'фантастика',
    'Ведьмак': 'фэнтази',
    'Клан Сопрано': 'криминал',
    '24': 'драма',
    'Черное зеркало': 'фантастика',
    'Во все тяжкие': 'криминал',
    'Игра престолов': 'фэнтази',
    'Карточный домик': 'драма',
    'Рик и Морти': 'фантастика'
}

# выводим информацию о жанре сериала ведьмак
print('Жанр сериала Ведьмак:', shows['Ведьмак'])

# выводим информацию на экран о всех сериалах
# данный цикл применим для вывода
for serial in shows.keys():
    print(serial)

# выводим на экран жанры
# создаем список уникальных жанров, проходим циклом по словарю, если жанра в списке нет то выводим на экран
shows_unique = []
for genre in shows.values():
    if genre not in shows_unique:
        print(genre)
        shows_unique.append(genre)