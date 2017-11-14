# -*-coding:UTF-8-*-


phrase = input("Введите предложение: ")


def entry(phrase_input):
    i = 0
    while phrase_input[i] != "е" and phrase_input[i] != "Е":
        i += 1
    else:
        print("первое вхожднние Буквы е  находиться на {} месте".format(i+1))
    j = len(phrase_input)-1

    while phrase_input[j] != "е" and phrase_input[j] != "Е":
        j -= 1
    else:
        print("Последнее вхожднние Буквы е  находиться на {} месте".format(j+1))

entry(phrase)

