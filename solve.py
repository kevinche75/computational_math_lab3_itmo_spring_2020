import methods
import graphics

def solve_equation():
    print("Доступные шаблоны уравнений: \n1. {0}\n2. {1}\n3. {2}".format(methods.F1.get_template(), methods.F2.get_template(), methods.F3.get_template()))
    print("Введите 1, 2 или 3")
    while True:
        try:
            number_method = int(input().strip())
            assert number_method <= 3 and number_method >= 1, "Введите число от 1 до 3"
            break
        except ValueError:
            print("Неверный формат числа. Введите число от 1 до 3")
        except AssertionError as inst:
            print(inst.args[0])

    if number_method == 1:

        print("Введите степень уравнения от 2 до 6")
        while True:
            try:
                count_n = int(input().strip())
                assert count_n <= 6 and count_n >= 2, "Введите число от 2 до 6"
                break
            except ValueError:
                print("Неверный формат числа. Введите число от 2 до 6")
            except AssertionError as inst:
                print(inst.args[0])
        
        print("Введите {0} коэффициента/ов для уравнения: \n{1} \n(Enter - чтобы подтвердить выбор коэффициента)".format(count_n+1, methods.F1.get_template()))
        coefs = []
        for i in range(count_n+1):

            while True:
                try:
                    coef = float(input().strip())
                    coefs.append(coef)
                    break
                except Exception:
                    print("Неверный формат числа. Попробуйте ещё раз")
        
        function = methods.F1(count_n, coefs)
    
    else:
        template = methods.F2.get_template() if number_method == 2 else methods.F3.get_template()
        print("Введите 3 коэффициента для уравнения: \n{0} \n(Enter - чтобы подтвердить выбор коэффициента)".format(template))

        coefs = []
        for i in range(3):

            while True:
                try:
                    coef = float(input().strip())
                    coefs.append(coef)
                    break
                except Exception:
                    print("Неверный формат числа. Попробуйте ещё раз")

        function = methods.F2(coefs) if number_method == 2 else methods.F3(coefs)

    print("Вы ввели: {0}".format(function.get_description()))

    print("Введите изначальный интервал - два числа через пробел (для метода простых итераций будет взято среднее)")
    while True:
        try:
            borders = input().split(" ")
            assert len(borders) == 2, "Введите два числа"
            borders[0] = float(borders[0])
            borders[1] = float(borders[1])
            assert borders[0] != borders[1], "Границы интервала не должны быть равны друг другу"
            break
        except ValueError:
            print("Не удалось распознать числа. Попробуйте ещё раз")
        except AssertionError as inst:
            print(inst.args[0])
    print("Введите точность")
    while True:
        try:
            eps = abs(float(input().strip()))
            break
        except Exception:
            print("Не удалось распознать число. Попробуйте ещё раз")

    if borders[0] > borders[1]:
        borders[0], borders[1] = borders[1], borders[0]
    bix_x = None
    fix_x = None
    try:
        if function(borders[0])*function(borders[1]) > 0:
            print("!Внимание: необходимое условие существования корней не выполнено. Результат может не являться приблеженным корнем уравнения")
        bis_i, bis_x, bis_log = methods.comp_bisection_method(*borders, function, eps)
        print("Метод половинного деления \nКоличество шагов: {0}\nПолученное приближенное решение: {1}\nf(x*) = {2}".format(bis_i, bis_x, function(bis_x)))
        graphics.draw_bis_method(bis_log, function, eps)
    except AssertionError as inst:
        print("Метод половинного деления: " + inst.args[0])
    try:
        fix_i, fix_x, fix_log = methods.comp_fixed_point_method(*borders, function, eps)
        print("Метод простых итераций \nКоличество шагов: {0}\nПолученное приближенное решение: {1}\nf(x*) = {2}".format(fix_i, fix_x, function(fix_x)))
        graphics.draw_fix_method(fix_log, function, eps)
    except AssertionError as inst:
        print("Метод простых итераций: " + inst.args[0])
    if bis_x != None and fix_x != None:
        graphics.draw_compare(function, eps, bis_x, fix_x)
    

def solve_set():

    print("Доступные шаблоны: \n{0} - для 2 неизвестных\n{1} - для 3 неизвестных".format(methods.F4.get_template(), methods.F5.get_template()))
    print("Введите количество неизвестных 2 или 3 (соответственно количество уравнений в системе)")
    while True:
            try:
                count_n = int(input().strip())
                assert count_n <= 6 and count_n >= 2, "Введите 2 или 3"
                break
            except ValueError:
                print("Неверный формат числа. Введите 2 или 3")
            except AssertionError as inst:
                print(inst.args[0])

    functions = []
    for i in range(count_n):
        
        template = methods.F4.get_template() if count_n == 2 else methods.F5.get_template()
        count_coefs = 6 if count_n ==2 else 10
        print("Введите {0} коэффициентов для уравнения: \n{1} \n(Enter - чтобы подтвердить выбор коэффициента)".format(count_coefs, template))

        coefs = []
        for i in range(count_coefs):

            while True:
                try:
                    coef = float(input().strip())
                    coefs.append(coef)
                    break
                except Exception:
                    print("Неверный формат числа. Попробуйте ещё раз")
        function = methods.F4(coefs) if count_n == 2 else methods.F5(coefs)
        functions.append(function)

    print("Вы ввели: ")
    for function in functions:
        print(function.get_description())
    print("Введите вектор приближений ({0} значения (Enter - чтобы подтвердить выбор значения))".format(count_n))

    vector_x_0 = []
    for i in range(count_n):
         while True:
                try:
                    x = float(input().strip())
                    vector_x_0.append(x)
                    break
                except Exception:
                    print("Неверный формат числа. Попробуйте ещё раз")

    print("Введите точность")
    while True:
        try:
            eps = abs(float(input().strip()))
            break
        except Exception:
            print("Не удалось распознать число. Попробуйте ещё раз")

    try:
        i, vector_x, log = methods.comp_newtons_method(vector_x_0, functions, eps)
        if count_n == 2:
            graphics.draw_newton_method_3d(log, functions, eps)
        else:
            graphics.draw_newton_method_4d(log, functions, eps)
        print("Количество шагов: {0}\nПолученное приближенное решение: {1}\nf_n(X*):".format(i, vector_x))
        for function in functions:
            print(function(*vector_x))
    except AssertionError as inst:
        print(inst.args[0])

if __name__ == "__main__":
    print("Что вы хотите решить: \n1.Уравнение\n2. Систему")
    print("Введите 1 или 2")
    while True:
        try:
            choose = int(input().strip())
            assert choose <= 2 and choose >= 1, "Введите 1 или 2"
            break
        except ValueError:
            print("Неверный формат числа. Введите 1 или 2")
        except AssertionError as inst:
            print(inst.args[0])
    if choose == 1:
        solve_equation()
    else:
        solve_set()
