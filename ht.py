# Задача 1. Напишите программу, которая принимает на вход вещественное число 
# и показывает сумму его цифр.

import os
os.system('cls||clear')
number = input('Введите вещественное число: ')
sumDigit = 0
for i in range(len(number)):
    if number[i] != '.':
        sumDigit += int(number[i])
print(sumDigit)


# Задача 2. Напишите программу, которая принимает на вход число N и выдает 
# набор произведений чисел от 1 до N. 

import os
os.system('cls||clear')
number = int(input('Введите число: '))
digit = 1
for i in range(1, number+1):
    digit = digit*i
    print(digit, end=' ')

# Задача 3. Задайте список из n чисел последовательности (1+1/n)^n и выведите на 
# экран их сумму. Пример: - Для n = 6:  [2.0, 2.25, 2.37037037037037, 2.44140625, 
# 2.4883199999999994, 2.5216263717421135]

import os
os.system('cls||clear')
number = int(input('Введите n: '))
spisok = [(1+1/i)**i for i in range(1, number+1)]
print(spisok)
print(f'Сумма: {sum(spisok)}')

# Задача 4. 1. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

import os
os.system('cls||clear')
number = int(input('Введите N: '))
spisok = [i for i in range(-number, number+1)]
print(f'заданный список: {spisok}')
with open('file.txt','r') as f:
    spisokF =f.read().split('\n')
print(f'позиции из файла: {spisokF}')

multiply = 1
for i in range(len(spisokF)):
    indSpisok = int(spisokF[i])
    multiply=multiply*spisok[indSpisok]
print(f'произведение: {multiply}')

#2. Реализуйте алгоритм перемешивания списка.
import random

for i in range(len(spisok)):
    ichange = random.randrange(0, len(spisok)-1)
    tmp = spisok[i]
    spisok[i] = spisok[ichange]
    spisok[ichange] = tmp
print(f'перемещанный список: {spisok}')
