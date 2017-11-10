# -*-coding:UTF-8-*-

phrase = input("Введите предложение: ")
symbol = input("Какой символ нужно найти? ")
for i in range(len(phrase)):
    if phrase[i] == symbol or phrase[i] == symbol.upper():
        print(phrase[i])