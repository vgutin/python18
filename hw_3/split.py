string1 = 'Съешь ещё этих мягких французских булок ДА выпей же чаю'

# разбиваем строку по пробелам, записываем в массив
str_arr = string1.split()

# записываем в переменную 4-е слово в верхнем регистре и выводим ее на экран
word4 = str_arr[3].upper()
print(word4)

# записываем в переменную 7-е слово в нижнем регистре и выводим ее на экран
word7 = str_arr[6].lower()
print(word7)

# записываем в переменную 3-ю букву в 8-м слове и выводим ее на экран
letters = list(str_arr[7])
letter3 = letters[2]
print(letter3)

# перебираем массив из слов и выводим каждое слово на экран
for word in str_arr:
    print(word)
