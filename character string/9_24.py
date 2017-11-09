# -*-coding:UTF-8-*-


# получить слова блок и око

inscr_1 = "яблоко"
print(inscr_1)
print(inscr_1[1:5])
print(inscr_1[3:])

# форма и тик

inscr_2 = "информатика"
print(inscr_2)
print(inscr_2[2:7])
print(inscr_2[7:10])

# получить слова тир и ветка.

inscr_3 = "вертикаль"
print(inscr_3)
print(inscr_3[3:5] + inscr_3[2])
print(inscr_3[0:2] + inscr_3[3] + inscr_3[5:7])

# получить слова ром и рампа
inscr_4 = "Программа"
print(inscr_4)
print(inscr_4[1:3]+inscr_4[6])
print(inscr_4[4:7] + inscr_4[0] + inscr_4[5])

# слова сорт, рост и торс.

inscr_5 = "трос"
print(inscr_5)
print(inscr_5[::-1])
print(inscr_5[1:]+inscr_5[0])
print(inscr_5[0] + inscr_5[2] + inscr_5[1] + inscr_5[3])

# получить слова уклон, кулон и колун.

inscr_6 = "клоун"

print(inscr_6)
print(inscr_6[3] + inscr_6[0:3]+ inscr_6[-1])
print(inscr_6[0] + inscr_6[-2] + inscr_6[1:3] + inscr_6[-1])
print(inscr_6[0] + inscr_6[-3] + inscr_6[1] + inscr_6[-2] + inscr_6[-1])

# спаниель.

inscr_7 = "апельсин"

print(inscr_7)
print(inscr_7[-3] + inscr_7[1::-1] + inscr_7[-1:-3:-1] + inscr_7[2:5])