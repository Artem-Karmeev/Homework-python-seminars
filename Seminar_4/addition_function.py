
def sum_dict(new_dict_1: dict, new_dict_2: dict):
    res_dict = {}

    if len(new_dict_2) > len(new_dict_1):
        res_dict.update(new_dict_2)
        res_dict.update(new_dict_1)
    else:
        res_dict.update(new_dict_1)
        res_dict.update(new_dict_2)

    for key in res_dict:
        res_dict[key] = new_dict_1.get(key, 0) + new_dict_2.get(key, 0)
    
    return res_dict
