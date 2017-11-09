# -*-coding:UTF-8-*-

inscription = input("ведите слово: ")
k = int(input("Какой символ показать: "))

print("{} символ слова {} это {}".format(k, inscription, inscription[k-1]))

