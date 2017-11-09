# -*-coding:UTF-8-*-

inscription = input("ведите слово: ")

if inscription[1] == inscription[3]:
    print("Второй и четвертый символы равны")
else:
    print("Второй и четвертый символы не равны")

if inscription[0] == inscription[len(inscription) - 1]:
    print("Первый и последний символы равны")
else:
    print("Первый и последний символы не равны")

