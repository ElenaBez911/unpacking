def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params('строка', True, 2)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [False, 329, 'True']
values_dict = {'a': 7, 'b': 'число', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3292, 'True/False']

print_params(*values_list_2, 42)