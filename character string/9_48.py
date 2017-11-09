# -*-coding:UTF-8-*-

inscription = input("Введите слово : ")
s_1 = ""
s_2 = ""
for i in range(4):
    s_1 += "+"
for i in range(5):
    s_2 += "-"
print(s_1 + inscription + s_2)