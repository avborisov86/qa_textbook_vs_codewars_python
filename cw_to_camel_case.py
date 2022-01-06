"""
Codewars:

Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was
capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text: str):
    import re
    # Делим входящую строку "text" по соответствующим симолам из класса, указанного в кавычках []
    words_list = re.split('[-_ .]', text)

    # Если строка не пустая, выполняем алгоритм
    if text.strip():
        new_words_list = []
        for word in words_list:
            title_word = word[0].upper() + word[1:].lower()
            new_words_list.append(title_word)
            if new_words_list[0][0] != words_list[0][0]:
                first_elem = new_words_list[0][0].lower() + new_words_list[0][1:]
                new_words_list[0] = first_elem
        return "".join(new_words_list)

    # В случае передачи пустой строки или строки с пробелами возвращаем пустую строку
    else:
        return "".join(words_list)


print(to_camel_case('The-Pippi_Is_kawaii'))
print(to_camel_case('A_pippi-was-Pippi'))
print(to_camel_case('A-Lenn_is.ill'))
print(to_camel_case('The-Lenn_is.ill'))
print(to_camel_case('A-B_C-D G.k'))
