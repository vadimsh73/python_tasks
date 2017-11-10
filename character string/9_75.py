# -*-coding:UTF-8-*-

phrase = input("Введите предложение: ")

i = 0
s = ""
while phrase[i] != ",":
    if i == len(phrase):
        print("Запятых не найдено")
        break
    else:
        s += phrase[i]
    i += 1
else:
    print(s)
