# -*-coding:UTF-8-*-

name = input("Введите название города")

if len(name) % 2 != 0:
    print("Количество символов нечетное")
else:
    print("Количество символов четное")