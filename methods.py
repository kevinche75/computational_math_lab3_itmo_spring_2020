from math import sin, cos
import numpy as np

limit = 10000

def comp_bisection_method(a, b, function, eps):

    log = []

    i = 1

    while(True):
        
        x = (a+b)/2
        log.append([a,b,x])
        if abs(a-b) <= eps or abs(function(x)) <= eps: break

        if function(a)*function(x) > 0:
            a = x
        else:
            b = x
        i+=1
        
        assert i < limit, "Не удалось найти решение за {0} итераций".format(limit)

    return i, x, log

def comp_fixed_point_method(a, b, function, eps):

    x = (a+b)/2
    log_values = [x]
    lambda_ = -1e+20
    step = a
    for i in range(int((b-a)/eps)):
        y = function.comp_derivative(step)
        lambda_ = max(lambda_, y)
        step += eps
    if lambda_ == 0:
        lambda_ = 1
    lambda_ = 1/lambda_

    i = 1

    while(True):
        x_0 = x
        try:
            x = x_0 - lambda_*function(x)
        except OverflowError:
            raise AssertionError("Произошло переполнение, не удалось найти решение")
        except ValueError:
            raise AssertionError("X вышел за границы float, не удалось найти решение")
        assert abs(1-lambda_*function.comp_derivative(x)) < 1, "Не удалось достичь сходимости"
        log_values.append(x)
        assert i < limit, "Не удалось найти решение за {0} итераций".format(limit)
        if abs(x_0 - x) < eps: break
        i+=1

    return i, x, {
        "lambda": lambda_,
        "logs": log_values
    }

def comp_newtons_method(vector_x, functions, eps):

    log = []
    vector_x = np.array(vector_x)
    log.append(vector_x)
    i = 1
    while(True):
        jacoby_m = []
        vector_f = []
        for function in functions:
            try:
                jacoby_m.append(function.comp_derivative(*vector_x))
                vector_f.append(function(*vector_x))
            except ValueError:
                raise AssertionError("Х вышел за границы float, не удалось найти решение")
        vector_x_0 = vector_x.copy()
        try:
            jacoby_m = np.linalg.inv(jacoby_m)
        except Exception:
            raise AssertionError("Не удалось найти обратную матрицу")
        delta_x = np.dot(jacoby_m, vector_f)
        vector_x = vector_x - delta_x
        log.append(vector_x)
        if max(abs(vector_x-vector_x_0))<eps:
            break
        assert i < limit, "Не удалось найти решение за {0} итераций".format(limit)
        i+=1
    return i, vector_x, np.array(log)

class F1(object):

    def __init__(self, n, coefs):

        self.n = n
        self.coefs = coefs

    def __call__(self, x):

        sum_f = self.coefs[0]

        for i in range(self.n):
            sum_f += (x**(i+1))*self.coefs[i+1]

        return sum_f

    def get_description(self):

        description = str(self.coefs[0])

        for i in range(self.n):
            description+="+{0}x^{1}".format(self.coefs[i+1], i+1)

        description += " = 0"

        return description
        
    @staticmethod
    def get_template():

        description = "c_0"

        for i in range(2):
            description+="+c_{0}*x^{1}".format(i+1, i+1)
        description +="...c_n+1*x^n"

        description += " = 0"

        return description

    def comp_derivative(self, x):

        sum_d = 0
        
        for i in range(self.n):
            sum_d += (x**(i))*self.coefs[i+1]*(i+1)

        return sum_d

class F2(object):

    def __init__(self, coefs):

        self.coefs = coefs

    def __call__(self, x):

        return self.coefs[0]*cos(self.coefs[1]*x) + self.coefs[2]*x

    def comp_derivative(self,x):

        return -self.coefs[0]*self.coefs[1]*sin(self.coefs[1]*x) + self.coefs[2]

    def get_description(self):
        return "{0}cos({1}x) + {2}x = 0".format(*self.coefs)

    @staticmethod
    def get_template():
        return "c_0*cos(c_1*x) + c_2*x = 0"


class F3(object):

    def __init__(self, coefs):

        self.coefs = coefs

    def __call__(self, x):

        return self.coefs[0]*(sin(self.coefs[1]*x))**2+self.coefs[2]*x

    def comp_derivative(self,x):

        return self.coefs[0]*self.coefs[1]*sin(2*self.coefs[1]*x)+self.coefs[2]

    def get_description(self):
        return "{0}sin({1}x)^2 + {2}x = 0".format(*self.coefs)

    @staticmethod
    def get_template():
        return "c_0*sin(c_1*x)^2 + c_2*x = 0"

class F4(object):

    def __init__(self, coefs):
        self.coefs = coefs

    def __call__(self, x, y):
        return self.coefs[0]*x**2 + self.coefs[1]*x+self.coefs[2]*x*y + self.coefs[3]*y + self.coefs[4]*y**2 + self.coefs[5]

    def comp_derivative(self,x,y):
        return [self.comp_derivative_x(x,y), self.comp_derivative_y(x,y)]

    def comp_derivative_x(self,x, y):
        return self.coefs[0]*2*x + self.coefs[1] + self.coefs[2]*y

    def comp_derivative_y(self,x,y):
        return self.coefs[2]*x + self.coefs[3] + self.coefs[4]*2*y

    def get_description(self):
        return "{0}x^2 + {1}x + {2}xy + {3}y + {4}y^2 + {5} = 0".format(*self.coefs)

    @staticmethod
    def get_template():
        return "c_0*x^2 + c_1*x + c_2*xy + c_3*y + c_4*y^2 + c_5 = 0"

class F5(object):

    def __init__(self, coefs):
        self.coefs = coefs

    def __call__(self, x, y, z):
        return self.coefs[0]*x**2 + self.coefs[1]*x + self.coefs[2]*x*y + self.coefs[3]*y + self.coefs[4]*y**2 + self.coefs[5]*y*z + self.coefs[6]*z+self.coefs[7]*z**2+self.coefs[8]*z*x + self.coefs[9]

    def comp_derivative(self,x,y,z):
        return [self.comp_derivative_x(x,y,z), self.comp_derivative_y(x,y,z), self.comp_derivative_z(x,y,z)]

    def comp_derivative_x(self,x, y, z):
        return self.coefs[0]*2*x + self.coefs[1] + self.coefs[2]*y + self.coefs[8]*z

    def comp_derivative_y(self,x,y, z):
        return self.coefs[2]*x + self.coefs[3] + self.coefs[4]*2*y + self.coefs[5]*z

    def comp_derivative_z(self,x,y,z):
        return self.coefs[5]*y + self.coefs[6] + 2 * self.coefs[7]*z + self.coefs[8]*x

    def get_description(self):
        return "{0}x^2 + {1}x + {2}xy + {3}y + {4}y^2 + {5}yz + {6}z + {7}z^2 + {8}zx + {9} = 0".format(*self.coefs)

    @staticmethod
    def get_template():
        return "c_0*x^2 + c_1*x + c_2*xy + c_3*y + c_4*y^2 + c_5*yz + c_6*z + c_7*z^2 + c_8*zx + c_9 = 0"