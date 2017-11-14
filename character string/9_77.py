# -*-coding:UTF-8-*-
phrase = input("Введите предложение: ")
letter = input("Какую букву ищем ")


def letter_sentence(phrase_input, letter_input):
    i = 0
    while phrase_input[i] != letter_input and phrase_input[i] != letter_input.upper():
        i += 1
    else:
        print("первое вхождение буквы {} находиться на {} месте".
              format(letter_input, i+1))


letter_sentence(phrase, letter)
