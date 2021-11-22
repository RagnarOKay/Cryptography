import re
from itertools import islice
from collections import Counter


def caeser_cipher(text, shift):

    alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

    result = ''
    text = text.upper()

    for i in text:
        place = alphabet_RU.find(i)
        new_place = place + shift
        if i in alphabet_RU:
            result += alphabet_RU[new_place]
        else:
            result += i
    return result


def many_lines(n, message):
    l = message.split()
    a = [' '.join(l[x:x+n]) for x in range(0, len(l), n)]
    for string in a:
        print(string)


def get_text(file_name):
    with open(file_name, encoding='utf-8') as file_object:
        result = ''
        for line in file_object:
            result += line
        return result


def get_monogram(message):
    alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ \n'

    f = {char: 0 for char in alphabet_RU}
    with open('original.txt', encoding='utf-8') as file:
        for line in file:
            for char in line:
                char = char.upper()
                if char != ' ':
                    char = char.upper()
                    if char in f.keys():
                        f[char] += 1
                    else:
                        f[char] = 1

    result = []
    letters = [' ', 'О', 'А', "Е", 'И', 'Н', 'Л',
                           'Р', 'С', 'В', 'К', 'М', 'Д', 'У', 'П',
                           'Б', 'Г', 'Т', 'Ы', 'Ч', 'Ь', 'З', 'Я', 'Й',
                           'Х', 'Ж', 'Ш', 'Ю', 'Ф', 'Э', 'Щ',
                           'Ё', 'Ц', 'Ъ']


    dictionary = dict(zip(f, letters))
    for i in message:
        if i in letters:
            result.append(dictionary.get(i))
            result.append(i)


    return ''.join(result)

def get_bigram(message, text):
    t = re.findall("\w{2}", text)
    bigr = Counter(islice(t, 1, None))

    t = re.findall("\w{2}", message)
    s_bigr = Counter(islice(t, 1, None))
    for i, y in zip(s_bigr.most_common(), bigr.most_common()):
        message = message.replace(i[0], y[0])

    return message


if __name__ == "__main__":

    original_text = get_text('original.txt')
    text = original_text.upper()
    print('Оригинальный текст')
    print(text)
    print('\n'*4)
    result = caeser_cipher(text, 3)
    print('\n'*4)
    print('Шифр Цезаря')
    print(result)
    m = get_monogram(result)
    print('\n'*4)
    print('Монограммы')
    print(many_lines(15, m))
    print('\n'*4)
    print('Биграммы')
    print(get_bigram(result, text))