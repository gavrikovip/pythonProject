# Семинар 4. Домашнее задание:
#    30. Вычислить число c заданной точностью d


# Точность d
d = 0.00001
number = 3.141545684123548993
print(number)

i = 0


def acc(d, i):
    while d < 1:
        d = d * 10
        i = i + 1
    return i


def accuracy(number):
    number = int(number * 10 ** j) / 10 ** j
    return print(number)


j = acc(d, i)
accuracy(number)

#    31. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Введите число N\n N = '))
for i in range(1, N + 1):
    if N % i == 0:
        print(i)

#    32. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

data = list(map(int, input('Введите последовательноть чисел через пробел:\n').split()))
res = []
[res.append(i) for i in data if i not in res]

print(f'Исходная последовательность: {data}')
print(f'Итоговая последовательность: {res}')

#    33. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

k = 2

#ax^2 + bx + c = 0
import random

a = random.randint(0, 101)
b = random.randint(0, 101)
c = random.randint(0, 101)
if a!=0 and b!=0 and c!=0:
    print(f'{a}x^{k} +{b}x +{c} = 0')
elif a!=0 and b!=0:
    print(f'{a}x^{k} +{b}x = 0')
elif a!=0 and c!=0:
    print(f'{a}x^{k} +{c} = 0')
elif b!=0 and c!=0:
    print(f'{b}x +{c} = 0')
elif b==0 and c==0:
    print(f'{a}x^{k} = 0')

#    34. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

poly1 = open('C:/Users/gip/Google Диск/Работа/git/Learning/Python/poly1.txt','r')
print(*poly1)
poly2 = open('C:/Users/gip/Google Диск/Работа/git/Learning/Python/poly2.txt','r')
print(*poly2)