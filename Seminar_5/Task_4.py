input_str = 'WWWNNRRRRRR'

def packing(input_str: str) -> str:
    input_str += ' '
    text_list = []
    count_list = []
    my_count = 1
    res_str = ''

    text_list.append(input_str[0])

    for i in range(1, len(input_str)):
        if input_str[i] == text_list[len(text_list)-1]:
            my_count += 1
        else:
            count_list.append(my_count)
            text_list.append(input_str[i])
            my_count = 1

    text_list.pop(len(text_list)-1)

    for i in range(len(text_list)):
        res_str += text_list[i] + str(count_list[i])

    return res_str

def inpack(packed_str: str) ->  str:
    inpack_str = ''
    for i in range(0, len(packed_str), 2):
        my_count = int(packed_str[i + 1])
        for _ in range(my_count):
            inpack_str += packed_str[i]
    return inpack_str

inpack_str = packing(input_str)
print(inpack_str)
print(inpack(inpack_str))
