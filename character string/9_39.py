# -*-coding:UTF-8-*-

# Переставить первые три и последние три буквы,
#  сохранив порядок их следования. Задачу решить двумя способами:

inscription = input("Введите слово : ")

inscription_1 = inscription[-3:] + inscription[3:-3] + inscription[0:3]
print(inscription_1)
inscription_2 = ""
inscription_3 = ""
for i in range(3):
    inscription_2 += inscription[i]
    inscription_3 += inscription[i-3]
print(inscription_3 + inscription[3:-3] + inscription_2)
