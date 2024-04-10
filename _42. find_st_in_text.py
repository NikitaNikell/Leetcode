def find_st(text, st):
    """ Имеются текст text и подстрока st.
    Напишите программу, которая находит индекс первого вхождения st в text. """
    if st in text:
        return text.index(st)
    return False


print(find_st("В роще-чаще рыщет ящер, ищет пищи подходящей", "ще"))