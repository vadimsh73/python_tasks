# -*-coding:UTF-8-*-

# Дано слово. Проверить, является ли оно "перевертышем"
#  (перевертышем на-зывается слово,
#  читаемое одинаково как с начала, так и с конца).

phrase = input("Введите предложение: ")


def palindrome(phrase_input):
    i = 0
    while phrase_input[i] == phrase_input[len(phrase_input)-i-1]:
        if i == len(phrase_input)//2:
            print("да")
            break
        i += 1
    else:
        print("Не Полиндром")


palindrome(phrase)
