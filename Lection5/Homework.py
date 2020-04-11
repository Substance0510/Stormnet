# № 1:
# def del_strings(l:list):
#     return [i for i in l if type(i) != str]
# print(*del_strings([1, 4, 12345, '1234', 5.6, '1']))

# № 2:
# def fibonachi(n:int):
#     fib_num1 = fib_num2 = 1
#     for i in range(n - 2):
#         fib_num1, fib_num2 = fib_num2, fib_num1 + fib_num2
#     return fib_num2
# print(fibonachi(12))

# № 3:
# def square_index(n:int):
#     return [i*i for i in range(n)]
# print(*square_index(7))

# № 4:
# import random
# def random_nums(n:int):
#     return [random.randint(1, n) for i in range(n)]
# print(*random_nums(6))

# № 5:
# def sum_even(l:list):
#     return sum((i for i in l if i % 2 == 0))
# print(sum_even([1, 3, 4, 6, 3, 9, 0, 8, 1]))

# № 6:
# def max_num(l:list):
#     return sorted(l, reverse=True)[0]
# print(max_num([9, 6, 3, 1, 6, 11, 9, 3]))