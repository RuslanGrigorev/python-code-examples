# 1
number = 7
number_string = str(number)
number_bool = bool(number)

# 2 - TypeError: can only concatenate str (not "int") to str

''' # 3 
Списки можно изменять, используются, когда нужно производить добавление, изменение, удаление элементов.
Кортежи неизменны, позволяют только читать элементы, используются, когда необходимо хранить коллекцию только для чтения.
'''

# 4
def numeric_operation(number):
    if type(number) is float:
        result = number ** 2 * 10
    else:
        result = 'Передано не числовое значение'
    print(result)

input_string = input('Введите данные для задания 4:')
input_number = float(input_string)

numeric_operation(input_string)
numeric_operation(input_number)

# 5
data = {
    'x': 1,
    'y': 2
}

if 'x' in data.keys():
    print('Ключ существует')

# 6
user = {
    'first_name': 'John',
    'last_name': 'Wick',
    'age': 99
}

def print_dict_v1(user):
    for key, value in user.items():
        print(f'{str(key)}: {value}')

def print_dict_v2(user):
    for key, value in user.items():
        result_key_string = ' '.join(i.capitalize() for i in str(key).split('_'))

        if type(value) is int:
            string_type_value = 'int'
        else:
            string_type_value = 'str'

        print(f'- {result_key_string}: {value} ({string_type_value})')

def print_dict_v3(user):
    unique_types = set()

    for value in user.values():
        if type(value) is int:
            string_type_value = 'int'
        else:
            string_type_value = 'str'
        unique_types.add(string_type_value)

    print(
        f'Quick stats:\n - {len(user)} keys ({", ".join(k for k in user.keys())})'
        f'\n - {len(unique_types)} unique types ({", ".join(type for type in unique_types)})'
        '\n Dict information:'
    )

    print_dict_v2(user)

print_dict_v1(user)
print_dict_v2(user)
print_dict_v3(user)