# положим, нам нужно сделать функцию
# которая не разрешит делать отрицательные ценники

def aplly_descount(product, discount):
    """
    принимает на вход данные о товаре и скидку
    """
    price = int(product['цена'] * (1.0 - discount))
    assert 0 <= price <= product['цена']
    return price, product['имя']


chair = {
    'имя': 'кресло',
    'цена': 12000
}

try:
    print(aplly_descount(chair, 1.25))
except AssertionError:
    print("А дурачок ты какие данные вводишь")
