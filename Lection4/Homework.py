# 1 max_number first variant:
# def max_of_all(*args):
#     return max(args)

# 1 max_number second variant:
# def max_of_all(*args):
#     return sorted(args, reverse=True)[0]

# 2 average_of_3:
# def average_of_3(a, b, c):
#     return sorted([a] + [b] + [c])[1]

# 2 average_of_all variant 2:
# def average_of_all(*args):
#     print(sorted(args)[len(args) // 2] if len(args) % 2 == 1 else 'Введите нечётное количество элементов.')

# 3 max_digit:
# def max_digit(in_num:int):
#     return int(sorted(str(in_num), reverse=True)[0])

# 4 reverse number
# def reversed_number(in_num:int):
#     return int(str(in_num)[::-1])

# 5 double digits
# def double_digits(in_lst:list):
#     return len([i for i in in_lst if len(str(i)) == 2])