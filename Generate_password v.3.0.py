print('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ ГЕНЕРАТОР ПАРОЛЯ', '*' * 20)

import random

length = int(input('Введите количество символов пароля '))
amount_p = int(input('Введите количество паролей для генерации '))
Password_g = input('Введите символы для генерации ')
pswrd = random.choice(Password_g)

for p in range(amount_p):
    password_generate = random.sample(Password_g, length)
    print('PASSWORD:', ''.join(password_generate))



