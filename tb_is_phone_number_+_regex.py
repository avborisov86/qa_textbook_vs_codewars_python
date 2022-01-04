"""
Textbook (page 222):

Предположим, требуется найти американский телефонный номер, содержащийся в строке.
Исходный текстовый шаблон известен: три цифры, дефис, три цифры, дефис, четыре цифры (например, 415-555-4242).

"""

import re


def is_phone_number(text):
    if len(text) != 12:
        return False  # not phone number-sized
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False  # not an area code
    if text[3] != '-':
        return False  # does not have first hyphen
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False  # does not have first 3 digits
    if text[7] != '-':
        return False  # does not have second hyphen
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False  # does not have last 4 digits
    return True  # "text" is a phone number!


print(is_phone_number('415-555-4242'))  # True
print(is_phone_number('415-555 4242'))  # False
print(is_phone_number('415-555-242'))  # False
print(is_phone_number('Moshi Moshi'))  # False
print(is_phone_number('578-479-2679'))  # True
print('')

# Вывод номеров телефонов, которые есть в строке сообщения.
"""
На каждой итерации цикла for в переменную chunk записываются очередные 12 последовательных символов строки 
message О. Например, на первой итерации i равно 0, а значит, переменной chunk присваивается срез 
message [0:12] (т.е. строка ’ Позвони мне '). На следующей итерации i равно 1, и переменной chunk присваивается 
срез message [1:13] (т.е. строка ' озвони мне з ’) и т.д.
Каждый такой фрагмент передается функции isPhoneNumber () , чтобы проверить, соответствует ли он образцу 
телефонного номера ®, и если результат проверки оказывается положительным, то найденный номер 
выводится на экран.
"""
message = 'Позвони мне завтра по номеру 415-555-1011. ' \
          '415-555-9999 - это номер телефона моего офиса.'
for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print('Найденный номер телефона: ' + chunk)
print('')

# Вывод номеров телефонов, которые есть в строке сообщения, с помощью регулярных выражений.
phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phone_num_regex.search('Мой номер: 888-333-2343')
print('Найденный код города и номер телефона с помощью регулярного выражения: ' + mo.group(), '\n')

phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phone_num_regex.search('Мой номер: 000-000-1111')
area_code, main_number = mo.groups()  # Метод возвращает кортеж и поэтому можно присваивать через операцию группирования
print(area_code)
print(main_number)
print('Найденный код города телефона с помощью регулярного выражения: ' + mo.group(1))
print('Найденный номер телефона без кода с помощью регулярного выражения: ' + mo.group(2))
print('Найденный код города и номер телефона с помощью регулярного выражения: ' + mo.group(), '\n')

# Пример 1 применения метода findall
xmas_regex = re.compile(r'\d{2}\s\w+')  # (\d{2}) - только 2 цифры
result = xmas_regex.findall('12 барабанщиков, 11 волынщиков, 10 лордов, 9 леди, 8 горничных, '
                            '7 лебедей, 6 гусей, 5 колец, 4 птицы, 3 курицы, 2 голубя, 1 куропатка')
print(result)

# Пример 2 применения метода findall
xmas_regex = re.compile(r'\d+\s\w+')  # (\d+) - одна или несколько цифр
result = xmas_regex.findall('12 барабанщиков, 11 волынщиков, 10 лордов, 9 леди, 8 горничных, '
                            '7 лебедей, 6 гусей, 5 колец, 4 птицы, 3 курицы, 2 голубя, 1 куропатка')
print(result)

# Пример 3 применения метода findall
xmas_regex = re.compile(r'\d\s\w+')  # (\d) - только 1 цифра
result = xmas_regex.findall('12 барабанщиков, 11 волынщиков, 10 лордов, 9 леди, 8 горничных, '
                            '7 лебедей, 6 гусей, 5 колец, 4 птицы, 3 курицы, 2 голубя, 1 куропатка')
print(result)

# Пример 4 применения метода findall с объявлением собственного класса для глассных букв
# [a-zA-ZO-9] - все буквы в нижнем и верхнем регистрах, а также цифры.
vowel_regex = re.compile(r'[aeiouAEIOU]')
result = vowel_regex.findall('RoboCAp Eats baby food. BABY FOOD.')
print(result)

# Пример 5 применения метода findall с объявлением собственного инвертированного класса (все кроме этих символов)
# [^aeiouAEIOU. ] - любые символы, кроме глассных буквы в нижнем и верхнем регистрах, точек и пробелов.
consonant_regex = re.compile(r'[^aeiouAEIOU. ]')
result = consonant_regex.findall('RoboCAp Eats baby food. BABY FOOD.')
print(result, '\n')

# Пример 6 применения метода search и регулярки (поиск строк с одной или несколькими цифрами)
"""
выражение '^\d+' - будет искать совпадения только в начале строки
выражение '\d+$' - будет искать совпадения только в конце строки
"""
wholestringls_num = re.compile(r'^\d+$')
print(wholestringls_num.search('1234567890'))
print(wholestringls_num.search('12345xyz67890'))
print(wholestringls_num.search('12 34567890'), '\n')

# Пример 7 применения метода findall и регулярки (точка - любой одиночный символ)
at_regex = re.compile(r'.at')
print(at_regex.findall('The cat in the hat sat on the flat mat.'), '\n')


# Пример 7 применения метода sub (замена искомой строки на указанную в методе) и регулярного выражения
namesRegex = re.compile(r'агент \w+', re.IGNORECASE)
result = namesRegex.sub('ЦЕНЗУРА', 'Агент Алиса передала секретные документы. Агент Боб.')
print(result)
