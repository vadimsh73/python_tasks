# -*-coding:UTF-8-*-

# Дано слово из четного числа букв. Поменять местами его половины. Задачу решить двумя способами:
# 1) без использования оператора цикла;
# 2) с использованием оператора цикла.

inscription = input("Введите слово: ")

print(inscription[len(inscription)//2:] + inscription[0:len(inscription)//2])

inscription_1 = ""
i = len(inscription)//2
while i != len(inscription):
    inscription_1 += inscription[i]
    print(inscription_1)
    i += 1
i = 0
while i != len(inscription)//2:
    inscription_1 += inscription[i]
    print(inscription_1)
    i += 1
