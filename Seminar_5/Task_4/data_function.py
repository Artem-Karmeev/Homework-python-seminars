def record_file(res: str):
    text = open("Seminar_5\Task_4\data\input_data.txt", 'w')
    text.writelines(res)
    text.close()

def read_file(link: str) -> str:
    text = open(link, 'r')
    res = text.read()
    text.close()
    return res

