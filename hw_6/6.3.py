import os

user_date = input('Введите дату: ')
user_note = input('Введите краткую запись о событиях на эту дату: ')

filename = 'blocknote.txt'

# устанавливаем флаги в зависимости от того существует ли файл
if os.path.exists(filename) is True:
    flag = 'r+'
else:
    flag = 'w+'

with open(filename, flag) as file:
    content = f'{user_date} : {user_note} \n'
    # если файл уже существует читаем его и выводим вместе с новой записью
    if flag == 'r+':
        exist_content = file.read()
        print(exist_content + content)
    else:
        print(content)
    file.write(content)
    file.close()
