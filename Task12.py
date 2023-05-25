# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
from math import sqrt

summa = input ("Введите сумму двух чисел: ")

while type(summa)!=int:
    try:
        summa = int(summa)
    except ValueError:
        print ("Ошибка!")
        summa = input ("Введите повторно сумму: ")

proiz = input ("Введите произведение двух чисел: ")

while type(proiz) != int:
    try:
        proiz = int(proiz)
    except ValueError:
        print ("Ошибка")
        proiz = input ("Введите повторно произведение: ")

y = int((summa - sqrt(summa**2-4*proiz))/2)
x = int((summa + sqrt(summa**2-4*proiz))/2)
if x<=1000 and y<=1000 and x+y==summa and x*y==proiz:
    print ("Петя загадал числа {0} и {1}" .format(int(y), int(x)))
else: 
    print ("Петя дал неправильные подсказки или числа неправильно загаданы")