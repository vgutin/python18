user_shows = {
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
user_ratings = {
    'Секретные материалы': 0.9,
    'Ведьмак': 0.95,
    'Клан Сопрано': 0.8,
    '24': 0.75,
    'Черное зеркало': 0.98,
    'Во все тяжкие': 0.85,
    'Игра престолов': 0.87,
    'Карточный домик': 0.82,
    'Рик и Морти': 1
}


def shows_by_genre(shows, genre):
    """
        Формирует список сериалов по заданному жанру\n
        Возвращает список сериалов соответствующих заданному жанру

        Parameters
        ----------
        shows : dict
        genre : str
    """
    result = []
    for key, value in shows.items():
        if value == genre:
            result.append(key)
    return result


def rating_averange(ratings, shows):
    """
        Вычисляет средний рейтинг заданных сериалов\n
        Принимает в качестве аргументов словарь с рейтингами сериалов
        и список сериалов, средний рейтинг которых необходимо вычислить
        Возвращает среднее значение рейтинга искомых сериалов

        Parameters
        ----------
        ratings : dict
        shows : list
    """
    ratio = 0
    count = 0
    for i in shows:
        ratio += ratings[i]
        count += 1
    return ratio / count, count


def shows_statistic(genre, shows, ratings):
    """
        Выводит на экран количество сериалов и средний рейтинг по заданному жанру\n
        Принимает в качестве аргумента искомый жанр, словарь сериалов и рейтингов
        используя функции shows_by_genre и rating_averange вычисляет количество сериалов
        в данном жанре и их средний рейтинг и выводит информацию на экран

        Parameters
        ----------
        genre : str
        shows : dict
        ratings : dict
    """
    show_list = shows_by_genre(shows, genre)
    ratio_show = rating_averange(ratings, show_list)
    print(f'Жанр: {genre} Количество сериалов: {ratio_show[1]} Средний рейтинг: {ratio_show[0]}')


shows_drama = shows_by_genre(user_shows, 'драма')
ratio_drama = rating_averange(user_ratings, shows_drama)
print('Среднее значений рейтинга сериалов в жанре "Драма":', ratio_drama[0])

shows_criminal = shows_by_genre(user_shows, 'криминал')
ratio_criminal = rating_averange(user_ratings, shows_criminal)
print('Среднее значений рейтинга сериалов в жанре "Криминал":', ratio_criminal[0])

unique_genries = set(user_shows.values())
for user_genrie in unique_genries:
    shows_statistic(user_genrie, user_shows, user_ratings)
