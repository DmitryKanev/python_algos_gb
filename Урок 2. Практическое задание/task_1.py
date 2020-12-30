"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, /
- условие завершения рекурсии - введена операция 0

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


def calculation():
    action = input('ведите тип операции (+, -, *, /), для выхода введите "0": ')
    if action == '+':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            result = a + b
            print(result)
            return calculation()
        except ValueError:
            print("Требуется ввести чило")
            return calculation()

    elif action == '-':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            result = a - b
            print(result)
            return calculation()
        except ValueError:
            print("Требуется ввести чило")
            return calculation()

    elif action == '*':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            result = a * b
            print(result)
            return calculation()
        except ValueError:
            print("Требуется ввести чило")
            return calculation()

    elif action == '/':
        try:
            a = int(input('Введите первое число: '))
            b = int(input('Введите второе число: '))
            result = a / b
            print(result)
            return calculation()
        except ValueError:
            print("Требуется ввести чило")
            return calculation()

    elif action == '0':
        print('Выход')



calculation()
