import random as r

# # Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# # Пример:
# # - 6782 -> 23
# # - 0,56 -> 11
# num = abs(float(input('Введите вещественное число: ')))
# sum = 0
# for i in str(num):
#     if i != '.':
#         sum = sum + int(i)
# print('Сумма цифр  равна ', sum)

# # Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# # Пример:
# # - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# num = abs(int(input('Введите число N: ')))
# i = 1
# multi = 1
# while i <= num:
#     multi *= i
#     i += 1
# print('Произведение чисел от 1 до N = ', multi)

# # Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# # Пример:
# # - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# # Первый вариант: формула как в примере
# number = int(input("Введите число N: "))
# ar = {}
# sum = 0
# for n in range(1, number+1):
#     ar[n] = 3 * n + 1
#     sum += ar[n]
# print(ar)
# print('Сумма элементов списка равна', sum)

# # Второй вариант: формула без непонятных символов
# number = int(input("Введите число N: "))
# ar = {}
# sum = 0
# for n in range(1, number + 1):
#     ar[n] = round(((1 + (1 / n)) ** n), 2)
#     sum += ar[n]
# print(ar)
# print('Сумма элементов списка равна', sum)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# Реализуйте алгоритм перемешивания списка.
num = abs(int(input('Введите целое число N: ')))
lst = [i for i in range(-num, num + 1)]
'''Заполняем список от -N до N.  
r.randint(-num, num + 1) - Заполнение случайными числами'''
print('Наш список:', lst)
path = 'file.txt'  # работа с текстовым файлом
text = open(path, 'w')  # запись в файл
for _ in range(num):
    text.write(f'{r.randint(1, num)}\n')
text.close()

multi = 1

text = open(path, 'r')  # чтение из файла
for _ in text:
    print(f'{_}')
    multi *= lst[int(_)]

print(f'Произведение равно {multi}')
text.close()


def shuffle_my_list(sm_list):
    for _ in range(len(sm_list)):
        k = r.randint(0, (len(sm_list) - 1))
        sm_list.append(sm_list.pop(k))


new_list = lst[:]
shuffle_my_list(new_list)
print(new_list)
