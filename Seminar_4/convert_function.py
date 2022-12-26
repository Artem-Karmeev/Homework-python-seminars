def convert_polynomial(my_dict):
    new_str = ''

    for key, value in my_dict.items():
        if value != 0 and value != 1 and value != -1 and key != 0:
            if key > 1:
                if value < 0:
                    new_str += str(value) + '*x' + '**' + str(key) + ' '
                else:
                    new_str += '+ ' + str(value) + '*x' + '**' + str(key) + ' '
            elif key == 1:
                if value < 0:
                    new_str += str(value) + '*x' + ' '
                else:
                    new_str += '+ ' + str(value) + '*x' + ' '
        if key == 0:
            if value > 0:
                new_str += '+ ' + str(value) + ' = 0'
            else:
                new_str += str(value) + ' = 0'

    if new_str[0] == '+':
        new_str = new_str[2: ]
    return new_str

def convert_str_in_dict(polynomial_str: str):
    polynomial_dict = {}
    new_list = []
    polynomial_str = polynomial_str.replace('*x ','*x**1 ').replace(' ', '').replace('+', '*x**').replace('-', '*x**-').replace('=', '*x**')

    if polynomial_str[0] == '*':
        polynomial_str = polynomial_str[4: ]

    new_list = polynomial_str.split('*x**')

    for i in range(0, len(new_list)-1, 2):
        polynomial_dict[int(new_list[i+1])] = int(new_list[i])
    return polynomial_dict