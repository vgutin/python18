import os, pickle

if not os.path.isfile('diary.dat'):
    data = [0, 1]
    data[0] = input('Введите тему')
    data[1] = input('Введите описание вашего дела')
    file = open('diary.dat', 'wb')
    pickle.dump(data, file)
    file.close()
else:
    file = open('diary.dat', 'rb')
    data = pickle.load(file)
    file.close()
    topic = input('Введите тему')
    info = input('Введите описание вашего дела')
    data.append(topic)
    data.append(info)
    file = open('diary.dat', 'wb')
    pickle.dump(data, file)
    file.close()
print(f'список ваших дел: {data[0]}, {data[1]}')
print(data)
