print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ГЕНЕРАТОР ПАРОЛЯ', '*' * 20)

import random

integer_g = '0123456789'
lowercase_g = 'qwertyuiopasdfghjklzxcvbnm'
uppercase_g = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols_g = '%?*-=+$#№@!~`^(){}[];:,.<>_/\\ '

length = int(input('Введите количество символов пароля '))

i=l=u=s = True

Password_g = ''

if i:
    Password_g += integer_g
if l:
    Password_g += lowercase_g
if u:
    Password_g += uppercase_g
if s:
    Password_g += symbols_g

for p in range(1):
    password_generate = ''.join(random.sample(Password_g, length))
    print('PASSWORD:',password_generate)
    print('Пароль сгенерирован')

    while True:
        e = input('Введите q для выхода ')
        if e == 'q': break
