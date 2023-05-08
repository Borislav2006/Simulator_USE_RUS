def read_text_file(file):
    """ Функция, возвращающая содержимое текстового файла """
    with open(file, encoding="utf-8") as file:
        text_in_file = file.read()
    return text_in_file
