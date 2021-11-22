


def alphabet(shift, key):
    a = ord('а')
    alphabet = ''.join([chr(i) for i in range(a,a+32)])
    for sym in key:
        alphabet = alphabet.replace(sym, '')
    alphabet = key + alphabet
    for i in range(shift):
        alphabet = alphabet[-1] + alphabet[:-1]
    return alphabet

def get_text(file_name):
    with open(file_name, encoding='utf-8') as file_object:
        result = ''
        for line in file_object:
            result += line
        return result

shift = int(input("shift: "))
key = input("key: ")
original_text = get_text('original.txt')

alphabet = alphabet(shift, key)
message = ''
for symbol in original_text:
    if symbol.isalpha():
        message += alphabet[(ord(symbol) - 224) %32 ]
    else:
        message += symbol


if __name__ == "__main__":
    print(message)
    print(alphabet)
