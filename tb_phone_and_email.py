"""
Textbook (page 244):

Предстоит заняться рутинной работой — найти все телефонные номера и адреса электронной почты,
которые содержатся на длинной веб-странице или в большом документе.

phone_and_email.py - Finds phone numbers and email addresses on the clipboard.

Страница с данными для примера работы программы: https://nostarch.com/contactus/
"""

import re
import pyperclip

# Регулярное выражение для поиска номера телефона
phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # код региона
    (\s|-|\.)?          # разделитель
    (\d{3})             # первые 3 цифры
    (\s|-|\.)           # разделитель
    (\d{4})             # последние 4 цифры
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # добавочный номер
)''', re.VERBOSE)

# Регулярное выражение для поиска номера телефона
email_regex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+      # имя пользователя
    @                      # @ символ
    [a-zA-Z0-9.-]+         # доменное имя
    (\.[a-zA-Z]{2,4}){1,2} # символ '.' и элементы после нее 
)''', re.VERBOSE)

# Поиск совпадений в скопированном тексте
text = str(pyperclip.paste())
matches = []
for groups in phone_regex.findall(text):
    phone_num = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_num += ' x' + groups[8]
    matches.append(phone_num)
for groups in email_regex.findall(text):
    matches.append(groups[0])

# Объединение совпадений в одну строку для копирования в буфер обмена
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Скопировано в буфер обмена:')
    print('\n'.join(matches))
else:
    print('Телефонные номера и адреса электронной почты не обнаружены.')
