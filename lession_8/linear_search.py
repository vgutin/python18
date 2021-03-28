from random import randint

data = list(range(1, 10000000))
#print(arr)

def random_generate(length):
    x = []
    for i in range(1, length):
        x.append(randint(1, length))
    return x

def search(arr, x):
    for i in range(1, len(arr)):
        if i == x:
            return i
    return -1

data2 = random_generate(100000)
#print(search(data, 75545))
print(search(data2, 75545))
