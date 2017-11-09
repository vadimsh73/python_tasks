# -*-coding:UTF-8-*-

name_1 = input("Первый город")
name_2 = input("Второй город")
name_3 = input("Третий город")

print("Максимальная длина {}".format(max(len(name_1), len(name_2), len(name_3))))
print("Минимальная длина {}".format(min(len(name_1), len(name_2), len(name_3))))

if max(len(name_1), len(name_2), len(name_3)) == len(name_1):
    print("максимально длинное название {}".format(name_1))
elif max(len(name_1), len(name_2), len(name_3)) == len(name_2):
    print("максимально длинное название {}".format(name_2))
else:
    print("максимально длинное название {}".format(name_3))

if min(len(name_1), len(name_2), len(name_3)) == len(name_1):
    print("Минимально длинное название {}".format(name_1))
elif min(len(name_1), len(name_2), len(name_3)) == len(name_2):
    print("Минимальноо длинное название {}".format(name_2))
else:
    print("Минимально длинное название {}".format(name_3))
