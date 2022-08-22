print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ГЕНЕРАТОР ПАРОЛЯ V.4.0', '*' * 5)

import random
import string

integer_g = string.digits
lowercase_g = string.ascii_lowercase
uppercase_g = string.ascii_uppercase
symbols_g = string.punctuation

length = int(input('Введите количество символов пароля '))
amount_p = int(input('Введите количество сгенерированных паролей '))

print('*** Для подтверждения конфигурации пароля введите "y" для отмены оставьте поле пустым и нажмите enter ***')

i = bool(input('Пароль должен содержать числа? '))

l = bool(input('Пароль должен содержать латинские буквы нижнего регистра? '))

u = bool(input('Пароль должен содержать латинские буквы верхнего регистра? '))

s = bool(input('Пароль должен содержать символы? '))

Password_g = ''

if i:
    Password_g += integer_g

if l:
    Password_g += lowercase_g

if u:
    Password_g += uppercase_g

if s:
    Password_g += symbols_g


for p in range(amount_p):
    password_generate = random.sample(Password_g, length)
    print('PASSWORD:', ''.join(password_generate))
