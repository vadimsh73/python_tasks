# -*-coding:UTF-8-*-

inscription_1 = input("ведите первое слово: ")
inscription_2 = input("ведите второе слово: ")

if inscription_1[0] == inscription_2[len(inscription_2)-1]:
    print("Первое слово начинается на ту же букву что и заканчиваеится второе слово ")
else:
    print("Буквы не совпадают")
