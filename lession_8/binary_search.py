# def binary_search(arr, low, hight, x):
#     global count
#     count += 1
#     #low = 0
#     #hight = len(arr)
#     mid = (low + hight) // 2
#     if count > len(arr):
#         return -1
#     else:
#         if arr[mid] == x:
#             return count
#         elif arr[mid] > x:
#             binary_search(arr, low, mid, x)
#         else:
#             binary_search(arr, mid, hight, x)

def binary_search(arr, x):
    count = 0
    x_low = arr[0]
    x_hight = arr[-1]
    while count < len(arr):
        count += 1
        x_mid = ((x_low + x_hight) // 2) - 1
        print(f'x_low({x_low}) x_hight({x_hight}) x_mid({x_mid + 1}) arr[x_mid]({arr[x_mid]})')
        if arr[x_mid] == x:
            return count
        elif arr[x_mid] > x:
            x_hight = x_mid
        else:
            x_low = x_mid

data = list(range(0, 10))
print(data)
x_count = binary_search(data, 4)
print(f'Число найдено за {x_count} итераций')