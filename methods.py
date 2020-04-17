from math import sin

limit = 10000

def bisection_method(a, b, function, eps):

    log = []

    i = 1

    while(True):
        
        x = (a+b)/2
        log.append([a,b,x])
        if function(a)*function(x) > 0:
            a = x
        else:
            b = x
        i+=1
        
        assert i < limit, "Не удалось найти решение за {0} итераций".format(limit)
        if abs(a-b) <= eps or abs(function(x)) < eps: break

    return i, x, log

def fixed_point_method(a, b, function, eps):

    log_values = []
    x = (a+b)/2
    lambda_ = 1/max(function.comp_derivative(a), function.comp_derivative(b))
    i = 1

    if lambda_ > 0:
        lambda_*=-1

    while(True):
        x_0 = x
        x = x_0 + lambda_*function(x)
        log_values.append([x_0, x])
        assert i < limit, "Не удалось найти решение за {0} итераций".format(limit)
        if abs(x_0 - x) < eps: break

    return i, x, {
        "lambda": lambda_,
        "logs": log_values
    }        
        

class F1(object):

    def __init__(self, n, coefs):

        self.n = n
        self.coefs = coefs

    def __call__(self, x):

        sum_f = self.coefs[0]

        for i in range(self.n):
            sum_f += (x**(i+1))*self.coefs[i+1]

        return sum_f

    def print_description(self):

        if self.coefs:

            description = "f(x) = " + str(self.coefs[0])

            for i in range(self.n):
                description+="+{0}x_{1}^{2}".format(self.coefs[i+1], i, i+1)

        else:
        
            description = "f(x) = c_0"

            for i in range(2):
                description+="+c_{0}*x_{1}^{2}".format(i+1, i, i+1)
            description +="...c_n+1*x_n^n"

        print(description)

    def comp_derivative(self, x):
        
        for i in range(self.n):
            sum_d += (x**(i))*self.coefs[i+1]*(i+1)

        return sum_d

    class F2(object):

        def __init__(self, coefs):

            self.coefs = coefs

        def __call__(self, x):

            assert x >= - self.coefs[1]/self.coefs[0], "Невозможно вычислить значение функции в точке {0}".format(x)

            return (self.coefs[0]*x+self.coefs[1])**(0.5)+self.coefs[2]

        def comp_derivative(self,x):

            assert x > - self.coefs[0]/self.coefs[1], "Невозможно вычислить значение производной в точке {0}".format(x)

        def print_description(self):

            if self.coefs:
                print ("sqrt({0}x+{1}) + {2}".format(*self.coefs))
            else:
                print ("sqrt({c_0*x+c_1) + c_3")

    class F3(object):

        def __init__(self, coefs):

            self.coefs = coefs

        def __call__(self, x):

            return self.coefs[0]*(sin(self.coefs[1]*x))**2+self.coefs[2]

        def comp_derivative(self,x):

            return self.coefs[0]*self.coefs[1]*sin(2*self.coefs[1]*x)

        def print_description(self):

            if self.coefs:

                print("{0}sin({1}x) + {2}".format(*self.coefs))

            else:

                print("c_0*sin(c_1*x) + c_2")