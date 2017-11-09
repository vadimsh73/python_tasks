# -*-coding:UTF-8-*-

inscription = input("Введите слово : ")
k = int(input("Сколько первых букв перенести в конец "))

# без использования оператора цикла;

print(inscription[k:] + inscription[0:k])

# с использованием оператора цикла.

#for i in range(k):
#    inscription += inscription[0]
#    inscription = inscription.replace(inscription[0], "", 1)
#print(inscription)

for i in range(k):
    inscription += inscription[0]
    inscription = inscription[1:]
print(inscription)
