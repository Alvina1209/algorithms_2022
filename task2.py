"""
Задание 2.
Реализуйте два алгоритма.
Оба должны обеспечивать поиск минимального значения для списка.
Сложность первого алгоритма должна быть O(n^2) - квадратичная.
Сложность второго алгоритма должна быть O(n) - линейная.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

##############################################################################
# Алгоритм:
# реализован механизм сортировки от наименьшего значения к наибольшему. При вызове функции возвращается первый эелемент
# списка, т.е. наименьший.
# Сложность: O(N^2)
def min_2(lst):
    for i in range(len(lst) - 1):                           # O(N)
        for j in range(len(lst) - i - 1):                   # O(N)
            if lst[j] > lst[j + 1]:                         # O(1)
                lst[j + 1], lst[j] = lst[j], lst[j + 1]     # O(1)
    return lst[0]

##############################################################################
# Алгоритм:
# осуществляется попарное сравнение элементов списка с помощью конструкции for .. in
# с присвоением переменной res наименьшего значения. В результате, при окончании итерирования, в переменной res будет
# находится наименьшее значение списка.
# Сложность: O(N)
def min_1(lst):
    res = lst[0]                    # O(1)
    for i in range(len(lst)):       # O(N)
        if lst[i] < res:            # O(1)
            res = lst[i]            # O(1)
    return res                      # O(1)

                                      # O(1)

list1 = [2, 5, 68, 0, -5]

print(min_1(list1))
print(min_2(list1))
