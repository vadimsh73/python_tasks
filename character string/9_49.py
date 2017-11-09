# -*-coding:UTF-8-*-

inscription = input("Введите слово : ")

s = ""
for i in range(len(inscription)):
    s += "*"
print(s + inscription + s)