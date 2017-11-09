# -*-coding:UTF-8-*-

inscription = input("Введите слово : ")

for i in range(0, len(inscription), 2):
    print(inscription[i], end="")
inscription_1 = ""
for i in range(len(inscription)-1, -1, -1):
    inscription_1 += inscription[i]
print(inscription_1)
