# -*-coding:UTF-8-*-


# Дано предложение. Напечатать все его буквы и.

phrase = input("Введите предложение: ")

for i in range(len(phrase)):
    if phrase[i] == "и" or phrase[i] == "И":
        print(phrase[i])