# Задача 10: На столе лежат n монеток. 
# Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

def minCoup (array):
    count0 = 0
    count1 = 0
    for i in range(len(array)):
        if array[i]==0: count0 +=1
        else: count1 +=1
    if count1>=count0: return count0
    else: return count1

size = input ("Введите количество монет на столе: ")

while type(size) != int:
    try:
        size = int(size)
    except ValueError:
        print ("Ошибка")
        size = input ("Введите повторно значение: ")

coins=[]

for i in range(size):
    coins.append(randint(0,1))

print (coins)

result = minCoup(coins)
print ("Мин. количество монет для разворорта {0}" .format(result))

