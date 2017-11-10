# -*-coding:UTF-8-*-

phrase = input("Введите предложение: ")

for i in range(len(phrase)+1):
    if i % 3 == 0 and i != 0:
        print(phrase[(i-1)])
