import sys


def main():
    """ Во входном файле (вы можете читать данные из файла input.txt) записан текст.
    Словом считается последовательность непробельных символов идущих подряд, слова разделены одним
    или большим числом пробелов или символами конца строки. Для каждого слова из этого текста подсчитайте,
    сколько раз оно встречалось в этом тексте ранее.
      """
    # Считываем входную строку
    s = list(map(str.strip, sys.stdin.readlines()))
    s1 = ' '.join(s).split()
    # Инициализируем словарь для отслеживания количества встреч слов
    word_count = {}

    # Проходимся по словам во входной строке
    for word in s1:
        # Если слово уже встречалось ранее, увеличиваем его счетчик
        if word in word_count:
            word_count[word] += 1
        else:
            # Иначе инициализируем счетчик для слова
            word_count[word] = 0

        # Выводим текущее значение счетчика для слова
        print(word_count[word], end=' ')

    print()


if __name__ == '__main__':
    main()


""" 
Input: 
She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.

Output:
0 0 0 0 0 0 1 0 0 1 0 0 1 0 2 2 0 0 0 0 1 2 3 3 1 1 4 0 1 0 1 2 4 1 5 0 0
"""
