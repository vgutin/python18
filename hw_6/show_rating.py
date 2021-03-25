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
