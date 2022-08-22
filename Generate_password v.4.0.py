print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ГЕНЕРАТОР ПАРОЛЯ V.4.0', '*' * 5)

import random

integer_g = '0123456789'
lowercase_g = 'qwertyuiopasdfghjklzxcvbnm'
uppercase_g = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbols_g = '%?*-=+$#№@!~`^(){}[];:,.<>_/\\ '

length = int(input('Введите количество символов пароля '))
count_p = int(input('Введите количество сгенерированных паролей '))

print('*** Для подтверждения конфигурации пароля введите (y) для отмены (n) ***')

i = bool(input('Пароль должен содержать числа? '))

l = bool(input('Пароль должен содержать латинские буквы нижнего регистра? '))

u = bool(input('Пароль должен содержать латинские буквы верхнего регистра? '))

s = bool(input('Пароль должен содержат символы? '))

Password_g = ''

if i== True:
    Password_g += integer_g

if l ==True:
    Password_g += lowercase_g

if u == True:
    Password_g += uppercase_g

if s==True:
    Password_g += symbols_g


for p in range(count_p):
    password_generate = random.sample(Password_g, length)
    print('PASSWORD:', ''.join(password_generate))
