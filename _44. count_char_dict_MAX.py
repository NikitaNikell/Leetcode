def letter_count(s):

    """Словарь для подсчета вхождений каждого символа в строке
    и затем найти символ с максимальным количеством вхождений."""

    chars = ''.join(s).replace(" ", "")
    char_count = {}

    for i in chars:
        char_count[i] = char_count.get(i, 0) + 1

    max_char = max(char_count, key=char_count.get)
    return f"Символ с максимальным количеством вхождений: {max_char}, число вхождений: {char_count[max_char]}"



print(letter_count("словарь для подсчета вхождений каждого символа в строке и затем найти символ с максимальным количеством вхождений."))