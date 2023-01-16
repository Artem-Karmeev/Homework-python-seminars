def record_file(res: str, link: str):
    text = open(link, 'w')
    text.writelines(res)
    text.close()

def read_file(link: str) -> str:
    text = open(link, 'r')
    res = text.read()
    text.close()
    return res

