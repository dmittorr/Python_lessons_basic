# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    if n > m:
        return
    a1 = 1
    a2 = 1
    aN = a2
    i = 2
    fib_list = [a1]
    while i < n:
        aN = a2 + a1
        a1 = a2
        a2 = aN
        i += 1
    fib_list.append(aN)
    for i in range(n, m-1, 1):
    # while i >= n and i < m:
        aN = a2 + a1
        a1 = a2
        a2 = aN
        # i += 1
        fib_list.append(aN)
    return fib_list[n-1:]


print(fibonacci(1, 9))


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    sorted_origin = []
    i = 0
    n = len(origin_list)
    while i < n:
        min_element = min(origin_list)
        sorted_origin.append(min_element)
        origin_list.remove(min_element)
        i += 1
    return sorted_origin



    # pass


print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

