def print_params(a=1, b='PC', c=True):
    print(a,b,c)

print_params()
print_params(b = 25)
print_params(c=[1, 2, 3])

values_list = [1, 'PC', True]
values_dict = {'a': 'Anton', 'b': 30, 'c': False}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['mom', 104]
print_params(*values_list_2, 42)
