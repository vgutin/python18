import show_rating as sr

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

shows_drama = sr.shows_by_genre(user_shows, 'драма')
ratio_drama = sr.rating_averange(user_ratings, shows_drama)
print('Среднее значений рейтинга сериалов в жанре "Драма":', ratio_drama[0])

shows_criminal = sr.shows_by_genre(user_shows, 'криминал')
ratio_criminal = sr.rating_averange(user_ratings, shows_criminal)
print('Среднее значений рейтинга сериалов в жанре "Криминал":', ratio_criminal[0])
