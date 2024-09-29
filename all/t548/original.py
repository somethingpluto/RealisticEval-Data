def read_txt_addjsonBracket(filename):
    with open(filename, encoding='utf-8') as data_file:
        text="["+data_file.read()
        text = text[:-2]+"]"
        data = json.loads(text)
    return data