# -*-coding:UTF-8-*-

# Дан текст. Определить количество букв "и" в первом предложении.
# Рассмотреть два случая:
# 1) известно, что буквы и в этом предложении есть;
# 2) букв и в тексте может не быть.


phrase = input("Введите предложение: ")
value = input("Введите значение поиска: ")


def number_of_letters(phrase_input, value_input):
    i = 0
    count_1 = 0
    while i < len(phrase_input):
        if phrase_input[i] == value_input:
            count_1 += 1
        i += 1
    return count_1


counts = number_of_letters(phrase, value)


if counts == 0:
    print("Символа {} нет в предложении ".format(value))
else:
    print("Символ {} встречается {} раз".format(value, counts))



