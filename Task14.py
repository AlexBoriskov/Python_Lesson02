# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

n = input ("Введите число N: ")

while type(n)!=int:
    try:
        n = int(n)
    except ValueError:
        print("Ошибка")
        n=input ("Введите повторно N: ")

stepen = []
count = 0
while 2**count <= n:
    stepen.append(count)
    count +=1

print (stepen)