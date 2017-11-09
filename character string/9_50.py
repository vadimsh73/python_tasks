# -*-coding:UTF-8-*-

inscription_1 = input("Введите первое слово : ")
inscription_2 = input("Введите второе слово : ")

for i in range(len(inscription_2)):
    inscription_1 = inscription_1.replace(inscription_1[i], inscription_2[i], 1)
print(inscription_1)