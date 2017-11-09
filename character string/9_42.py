# -*-coding:UTF-8-*-

inscription = input("Введите слово : ")

for i in range((len(inscription) - 1), -1, -1):
    print(inscription[i], end="")
