# -*-coding:UTF-8-*-

symbol = input("Введите символ: ")
number = int(input("Введите количество символов"))
s = ""
for i in range(number):
    s += symbol
print(s)