import random

print("Вас приветствует программа виртуального казино. Вам предоставляется депозит в 10 000 единиц.Загадайте число, я брошу кубики")
account = 10000

while account > 0:
    user_dice = input("Выберете число от 1 до 12")
    while True:
        try:
            user_dice = int(user_dice)
            if user_dice > 0 and user_dice < 13:
                break
            else:
                user_dice = input("Ошибка ввода. Выберете число от 1 до 12")
        except ValueError:
            user_dice = input("Ошибка ввода. Введите целочисленное значение от 1 до 12")

    ai_dice = random.randint(1, 12)
    if ai_dice == user_dice:
        print("Поздравляю! Вы выйграли 12000")
        account += 12000
    else:
        print("Увы! Вы проиграли 1000")
        account -= 1000

    if account == 0:
        print("На вашем счету 0. Игра завершена")
    else:
        print("На вашем счету:", account)