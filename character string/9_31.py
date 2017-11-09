# -*-coding:UTF-8-*-
# фокус
inscr_1 = "вирус"
print(inscr_1)
inscr = inscr_1.replace("вир", "фок")
print(inscr_1)

# танцор.
inscr_2 = "курсор"
print(inscr_2)
inscr_2 = inscr_2.replace("курс", "танц")
print(inscr_2)

# продел
inscr_3 = "пробел"
print(inscr_3)
inscr_3 = inscr_3.replace(inscr_3[-3], "д")
print(inscr_3)

# Строфа

inscr_4 = "строка"
print(inscr_4)
print(inscr_4.replace(inscr_4[-2], "ф"))

inscr_5 = "муха"
inscr_6 = "тетрадь"

print(inscr_5)
print(inscr_5.replace("муха", "слон"))

print(inscr_6)
print(inscr_6.replace("тетрадь", "дневник"))