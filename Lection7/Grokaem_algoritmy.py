#binary_search:
# def binary_search(l:list, item):
#     left = 0
#     right = len(l) - 1
#
#     while left <= right:
#         middle = (left + right) // 2
#         guess = l[middle]
#         if guess == item:
#             return middle
#         elif guess > item:
#             right = middle - 1
#         else:
#             left = middle + 1
#     return None
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))