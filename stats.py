def sort_on(items):
    return items["num"]

def parse_dict(dic):
    array_dic = []
    for k, v in dic.items():
        array_dic.append({"char": k, "num": v}) 
    array_dic.sort(reverse=True, key=sort_on)
    return array_dic

def get_book_dict(text):
    letters = {}
    for t in text:
        letters[t] = letters.get(t, 0) + 1
    return parse_dict(letters)

def get_book_data(path):
    with open(path) as f:
        text = f.read().lower()
        return get_num_and_dic(text)

def get_num_and_dic(text):
    return len(text.split()), get_book_dict(text)
