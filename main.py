import math
retry = 1
password = input('Подтвердите, что вы не робот, введите "@":')
if password != '@':
    print('Вы не прошли проверку, вы робот, тогда зачем вам калькулятор? :/')
else:
    print('Вы успешно прошли проверку!')
    print('Привет! Добро пожаловаать в калькулятор.')
    while retry == 1:
        print('Выберите действие, которое хотите совершить: \n'
              '+ : сложение; \n'
              '- : вычитание; \n'
              '/ : деление; \n'
              '* : умножение; \n'
              '** : возведение в степень + любое целое число; \n'
              'x : квадратное уравнение.')
        operator = input()
        if operator == '+':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 + number_2
            print('ответ = ', res)
        elif operator == '-':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 - number_2
            print('ответ = ', res)
        elif operator == '*':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 * number_2
            print('ответ = ', res)
        elif operator == '/':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 / number_2
            print('ответ = ', res)
        elif operator == '**':
            number_1 = float(input('Введите первую переменную:'))
            number_2 = float(input('Введите вторую переменную:'))
            res = number_1 ** number_2
            print('ответ = ', res)
        elif operator == 'X':
            a = float(input('Введите a:'))
            b = float(input('Введите b:'))
            c = float(input('Введите c:'))
            dt = b ** 2 - 4 * a * c
            if dt == 0:
                x1 = -b / (2 * a)
                print('x = ', x1)
            elif dt > 0:
                x1 = (-b + math.sqrt(dt)) / (2 * a)
                x2 = (-b - math.sqrt(dt)) / (2 * a)
                print('x1= ', x1, '\nx2= ', x2)
            else:
                print('Корней нет')

        else:
            print('неизвестная операция')




