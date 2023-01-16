 
def convert_list_in_str(li: list) -> str:
    li = list(zip(li[0], li[1]))
    li = [str(li[i][0]) + li[i][1] for i in range(len(li))]
    li =''.join(li)
    return li

def packing(data: str) -> list:
    tmp_list = [[], []]
    data+= ' '
    temp_i = 1

    tmp_list[1].append(data[0])

    for i in range(1, len(data)):
        if data[i] == tmp_list[1][len(tmp_list[1])-1]:
            temp_i += 1
        else:
            tmp_list[0].append(temp_i)
            tmp_list[1].append(data[i])
            temp_i = 1
    return convert_list_in_str(tmp_list)

def inpack(packed_str: str) ->  str:
    inpack_str = ''
    for i in range(0, len(packed_str), 2):
        my_count = int(packed_str[i + 1])
        for _ in range(my_count):
            inpack_str += packed_str[i]
    return inpack_str