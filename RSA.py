import random
import math


prime_numbers = []
for num in range(1, 1001, 2):
    if all(num % i != 0 for i in range(3, int(math.sqrt(num)) + 1, 2)):
        prime_numbers.append(num)

alphabet_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !?.,;:\n-'


while True:

    x = int(input('Введите p параметр: '))
    if x not in prime_numbers:
        print('Вы ввели не простое число, повторите попытку')
    else:
        y = int(input('Введите q параметр: '))
        if y not in prime_numbers:
            print('Вы ввели не простое число, повторите попытку')
        else:
            break


def function_Euler(p, q):
    result = (p-1)*(q-1)
    print('Функция Эйлера: ' + str(result))
    return result

a = function_Euler(x, y)
mod = x * y


def open_exponent():

    da = True
    while da:
        num = random.randint(1, 100)
        if num in prime_numbers and num < a and a % num != 0:
            right_num = num
            da = False
    print("Свободная экспонента: " + str(right_num))
    return right_num

def num_d():

    i = True
    z = 0
    right_d = 0
    while i:
        d = prime_numbers[z]
        da = o_e * d % a == 1
        if da:
            right_d = d
            i = False
        else:
            z += 1
    print('Число d: ' + str(right_d))
    return right_d

o_e = open_exponent()
n_d = num_d()

def encrypted_and_decrypted_word(word):
    #w = word.lower()
    #s = list(w)
    input = word
    input = input.lower()
    output=[]
    output_mod = []
    dec_numbers = []
    dec_output = []

    for character in input:
        number = alphabet_RU.index(character)
        output.append(number)
    print(output)


    for numbers in output:
        mod_num = pow(numbers, o_e) % mod
        output_mod.append(mod_num)
    print(output_mod)


    for numbers_decrypted in output_mod:
        dec_num = pow(numbers_decrypted, n_d) % mod
        dec_numbers.append(dec_num)
    print(dec_numbers)


    for numb in dec_numbers:
        dec_word = alphabet_RU[numb]
        dec_output.append(dec_word)
    print(dec_output)


    dec_output = ''.join(dec_output)
    print(dec_output.capitalize())

if __name__ == '__main__':

 encrypted_and_decrypted_word('короче, меченый, я тебя спас и в '
                              'благородство играть не буду: выполнишь '
                              'для меня пару заданий и мы в расчете. '
                              'Заодно посмотрим, как быстро у тебя башка '
                              'после амнезии прояснится. а по твоей теме '
                              'постараюсь разузнать. хрен его знает, на кой ляд '
                              'тебе этот стрелок сдался, но я в чужие дела не лезу, '
                              'хочешь убить, значит есть за что')

