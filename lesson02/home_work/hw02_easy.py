# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()
print("Задача-1: ")
fruit_list = ["яблоко", "банан", "киви", "арбуз"]
i = 1
for fruit in fruit_list:
    print(str(i) + '.', fruit.rjust(8, ' '))
    i = i + 1
print()
# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print("Задача-2: ")
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 4, 2, 6, "яблоко", "банан", "киви", "арбуз"]

my_list2 = [2, 4, 6, 8, "банан", "киви"]


i = 0
for el2 in my_list2:
    if el2 in my_list1:
        i = 0
        while i < len(my_list1):
            if el2 == my_list1[i]:
                my_list1.pop(i)
            else:
                i += 1

print(my_list1)
print(my_list2)
print()

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.
print("Задача-3: ")
my_list1 = [1, 2, 3, 4, 5, 6, 7, 8]
i = 0
while i < len(my_list1):
    if (my_list1[i] % 2) == 0:
        my_list1[i] = my_list1[i] / 4
    else:
        my_list1[i] = my_list1[i] * 2
    i += 1
print(my_list1)
