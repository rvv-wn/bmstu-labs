"""
Автор: Воробьев Рустам Сергеевич
Группа: ИУ7-14Б
Вариант: 85
Сумма бесконечного ряда
"""

from math import pi

eps = 1e-10  # Очень маленькое число для проверки на 0
M = 1e10  # Очень большое число для проверки корректности
flag = True

# Ввод данных
if flag:
    x = float(input('Введите "x": '))
    if x > M:
        print("Входные данные некорректныы")
        flag = False
if flag:
    E = float(input("Введите точность: "))

    if E > M or E < eps:
        print("Входные данные некорректны")
        flag = False
if flag:
    h = float(input("Введите шаг печати: "))
    if h > M or abs(h - int(h)) > eps or h <= 0:
        print("Входные данные некорректны")
        flag = False
    else:
        h = int(h)
if flag:
    max_it = float(input("Введите максимальное число итераций: "))
    if max_it > M or abs(max_it - int(max_it)) > eps or max_it <= 0:
        print("Входные данные некорректны")
        flag = False
    else:
        max_it = int(max_it)

if flag:
    # Ввод изначальных значений
    s = 0
    el = 1
    n = 0
    el_h = x
    flag_it = False
    # Вывод заголовка таблицы
    print(
        "-" * 47
        + "\n| № итерации "
        + f"|{'h':^15}|"
        + f"{'s':^16}|"
        + "\n|"
        + 45 * "-"
        + "|"
    )
    # Расчет значений
    while abs(el) > E:
        # Изменение суммы
        s += el
        # Вывод строки таблицы со значением
        if (n - 1) % h == 0:  # and n != 0:
            print(f"| {n:<11}|" + f" {el:<13.6g} |" + f"  {s:<13.6g} |")
        # Проверка на превышение лимита итераций
        if n == max_it:
            flag_it = True
            break
        n += 1
        # Оптимизация вычисления степени и факториала
        el_h *= x / n
        # Расчет следующего элемента
        el = (n * pi / 4) * el_h
    print("-" * 47)
    # Проверка превышения лимита операций
    if flag_it:
        print("Превышен лимит операций\n")
    if 2 <= n % 10 <= 4:
        ending = "и"
    elif n % 10 == 1:
        ending = "ю"
    elif 12 <= n % 100 <= 14:
        ending = "й"
    else:
        ending = "й"
    print(
        f"Сумма бесконечного ряда - {s:.6g}, вычисленна за {n} итераци" + ending + "."
    )
