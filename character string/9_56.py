# -*-coding:UTF-8-*-

phrase = input("Введите предложение: ")
symbol = input("Сочетание каких символов искать? ")

for i in range(len(phrase)):
    if i != 0 and phrase[i] == symbol and phrase[i-1] == symbol:
        print(phrase[i-1] + phrase[i])
