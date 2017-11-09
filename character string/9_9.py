# -*-coding:UTF-8-*-

last_name_1 = input("Введите первую фамилию")
last_name_2 = input("Введите вторую фмилию ")

if len(last_name_1) > len(last_name_2):
    print("Первая фамилия длиннее второй")
elif len(last_name_2) > len(last_name_1):
    print("Вторая фамилия длиннее первой")
else:
    print("Длинна фамилий равны")