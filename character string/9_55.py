# -*-coding:UTF-8-*-

phrase = input("Введите предложение: ")

symbol_1 = input("Какой 1 символ нужно найти? ")
symbol_2 = input("Какой 2 символ нужно найти? ")

for i in range(len(phrase)):
    if phrase[i] == symbol_1 or phrase[i] == symbol_1.upper() or \
        phrase[i] == symbol_2 or phrase[i] == symbol_2.upper():
        print(phrase[i])
