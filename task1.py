# Задача 1. Напишите программу, которая принимает на вход число N 
# и выдает список факториалов для чисел от 1 до N.

def factorialN(number):
    result = 1
    while number > 1:
        result = result * number
        number = number - 1
    return result

num = int(input('Введите число: '))

for i in range(1, num + 1):
    print(factorialN(i), end=' ')
