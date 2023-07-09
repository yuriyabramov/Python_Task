# Требуется найти в массиве list_1 самый близкий по 
# величине элемент к заданному числу k и вывести его.
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 2, 3, 4, 5]
k = 6
def nearest_k(list_1, k):
    found = list_1[0] 
    for i in list_1:
        if abs(i - k) < abs(found - k):
            found = i
    return found
print(nearest_k(list_1, k))


# find_num = int()       
# for i in range(len(list_1)):
#     if list_1[i] < k:
#         find_num = -find_num
#     else:
#         find_num = find_num + 0
#     if list_1[i] >= k and list_1[i] - k <= find_num - k:
#         find_num = list_1[i]
#     elif list_1[i] <= k and find_num - k <= list_1[i] - k:
#         find_num = list_1[i]
# print(find_num)