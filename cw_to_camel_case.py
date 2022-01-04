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
    text_list = re.split('[-_]', text)
    return text_list

    # if '-' in text:
    #     text_list = text.split('-')
    #     new_text_list = []
    #
    #     if text_list[0].islower():
    #         new_text_list = [text_list[0]]
    #         for elem in text_list[1:]:
    #             if elem.islower():
    #                 el = elem.capitalize()
    #                 new_text_list.append(el)
    #
    #     else:
    #         for elem in text_list:
    #             if elem.islower():
    #                 el = elem.capitalize()
    #                 new_text_list.append(el)
    #             else:
    #                 new_text_list.append(elem)
    #
    #     return "".join(new_text_list)
    #
    # else:
    #     text_list = text.split('_')
    #     new_text_list = []
    #
    #     if text_list[0].islower():
    #         new_text_list = [text_list[0]]
    #         for elem in text_list[1:]:
    #             if elem.islower():
    #                 el = elem.capitalize()
    #                 new_text_list.append(el)
    #
    #     else:
    #         for elem in text_list:
    #             if elem.islower():
    #                 el = elem.capitalize()
    #                 new_text_list.append(el)
    #             else:
    #                 new_text_list.append(elem)
    #
    #     return "".join(new_text_list)


print(to_camel_case('the_stealth-Warrior'))
