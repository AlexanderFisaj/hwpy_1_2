# Задача 4. Задайте список из N элементов, 
# заполненных числами из промежутка [-N, N]. 
# Сдвиньте все элементы списка на 2 позиции вправо.

from random import randint

number = int(input('Введите количество элементов: '))
shift = int(input('Введите количество элементов для сдвига: '))
number = abs(number * 2 + 1)
list = []
temp = []

for i in range(number):
    list.append(randint(-number, number + 1))

print(f'Список до смещения {list}')

for j in range(shift):
    temp.append(list[j])

for k in range(len(list) - shift):
    list[k] = list[k + shift]    

for l in range(len(temp)):
    list[-shift+l] = temp[l]

print(f'Список после смещения {list}')