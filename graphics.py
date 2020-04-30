import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np
import methods

def draw_bis_method(log, function, eps):
    fig, ax = plt.subplots()
    a = log[0][0]
    b = log[0][1]
    data_x = []
    data_y = []

    step = eps
    n_steps = int(abs(a-b)/eps)+22

    x = a-10*step
    for i in range(n_steps):
        x += step
        data_x.append(x)
        data_y.append(function(x))
    ax.plot(data_x,data_y)
    ax.plot([a,a], [0,function(a)], 'r--')
    ax.plot([b,b], [0, function(b)], 'r--')
    ax.grid()
    line, = ax.plot([a-step, b+step], [0,0], 'black')

    def init():
        line.set_data([], [])
        plt.xlabel('X')
        plt.ylabel('f(x)')
        plt.title('Метод половинного деления: {0}\nЗеленая точка - решение'.format(function.get_description()))
        return line,

    def animate_bis(i):
        c = log[i][2]
        if i != len(log)-1:
            ax.plot([c,c], [0, function(c)], 'r--')
        else:
            ax.plot([c,c], [0, function(c)], 'g--')
            ax.scatter(c, function(c), c = 'g', label = "x*")
        plt.xlabel('X')
        plt.ylabel('f(x)')
        plt.title('Метод половинного деления: {0}\nЗеленая точка - решение'.format(function.get_description()))
        return line, ax

    ani = FuncAnimation(fig, animate_bis, frames=len(log), interval=1000, blit = True, init_func=init)
    plt.show()

def draw_fix_method(log, function, eps):
    fig, ax = plt.subplots()
    lambda_ = log["lambda"]
    logs = log["logs"]
    a = min(logs)
    b = max(logs)
    data_x = []
    data_y = []

    step = eps
    n_steps = int(abs(a-b)/step)+22

    x = a-10*step
    for i in range(n_steps):
        x += step    
        data_x.append(x)
        data_y.append(x-lambda_*function(x))
    ax.plot(data_x,data_y, 'b')
    ax.plot([a-10*step, b+10*step], [a-10*step,b+10*step], 'b')
    ax.grid()
    line, = ax.plot([],[])

    def init():
        line.set_data([], [])
        plt.xlabel('X')
        plt.ylabel('f(x)')
        plt.title('Метод простой итерации: {0}\nЗеленая точка - решение'.format(function.get_description()))
        return line,

    def animate_bis(i):
        x_0 = logs[i]
        x = logs[i+1]
        if i != len(logs)-2:
            ax.plot([x_0,x_0, x], [x_0, x, x], 'r--')
        else:
            ax.plot([x_0,x_0, x], [x_0, x, x], 'g--')
            ax.scatter(x, x, c ='g', label = "x*")
        plt.xlabel('X')
        plt.ylabel('f(x)')
        plt.title('Метод простой итерации: {0}\nЗеленая точка - решение'.format(function.get_description()))
        return line, ax

    ani = FuncAnimation(fig, animate_bis, frames=len(logs)-1, interval=1000, blit = True, init_func=init)
    plt.show()

def draw_compare(function, eps, x1 = None, x2 = None):

    fig, ax = plt.subplots()
    
    a = min(x1, x2)
    b = max(x1, x2)
    data_x = []
    data_y = []
    
    step = eps
    n_steps = int((b-a)/eps)+20
    x = a - 10*step
    for i in range(n_steps):
        x += step
        data_x.append(x)
        data_y.append(function(x))
    ax.plot(data_x,data_y)
    ax.grid()
    ax.scatter(x1, function(x1), c = 'r', label = "Метод половинного деления")
    ax.scatter(x2, function(x2), c = 'g', label = "Метод простых итераций")
    ax.legend()
    plt.show()



def draw_newton_method_3d(log, functions, eps, labels = None):
    if labels:
        label_0 = labels[0]
        label_1 = labels[1]
        label_2 = labels[2]
        label_3 = labels[3]
    else:
        label_0 = '(x*,y*)'
        label_1 = 'f(x,y)'
        label_2 = 'x'
        label_3 = 'y'
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    step = eps
    a = np.min(log)
    b = np.max(log)
    n_steps = int((b-a)/step)+22

    for function in functions:
        z = []
        xval = np.linspace(a-10*step, b+10*step, n_steps)
        yval = np.linspace(a-10*step, b+10*step, n_steps)
        x, y = np.meshgrid(xval, yval)
        for i in range(n_steps):
            raw_z = []
            for j in range(n_steps):
                raw_z.append(function(x[i,j], y[i,j]))
            z.append(raw_z)
        surf = ax.plot_surface(x, y, np.array(z), alpha = 0.3, label = function.get_description())
        surf._facecolors2d=surf._facecolors3d
        surf._edgecolors2d=surf._edgecolors3d
    x = log[-1,0]
    y = log[-1,1]
    ax.scatter(x,y,functions[0](x,y), s=0.5, c='r', label = label_0)
    ax.grid()
    ax.set_title('Метод Ньютона')
    ax.set_xlabel(label_2)
    ax.set_ylabel(label_3)
    ax.set_zlabel(label_1)
    ax.legend()
    plt.show()

def draw_newton_method_4d(log, functions, eps):
    
    functions_z_0 = []
    functions_y_0 = []
    functions_x_0 = []
    x,y,z = log[-1]

    for function in functions:
        coefs = function.coefs
        functions_z_0.append(methods.F4([coefs[0],
                                         (coefs[1]+coefs[8]*z),
                                         coefs[2],
                                         (coefs[3]+coefs[5]*z),
                                         coefs[4],
                                         (coefs[6]*z+coefs[7]*z**2+coefs[9])]))
        functions_y_0.append(methods.F4([coefs[0],
                                         (coefs[1]+coefs[2]*y),
                                         coefs[8],
                                         (coefs[6]+coefs[5]*y),
                                         coefs[7],
                                         (coefs[3]*y+coefs[4]*y**2+coefs[9])]))
        functions_x_0.append(methods.F4([coefs[4],
                                         (coefs[3]+coefs[2]*x),
                                         coefs[5],
                                         (coefs[6]+coefs[8]*x),
                                         coefs[7],
                                         (coefs[1]*x+coefs[0]*x**2+coefs[9])]))
    
    draw_newton_method_3d(log[:,0:2], functions_z_0, eps, ['(x*,y*)', 'f(x,y,z*)', 'x', 'y'])
    draw_newton_method_3d(log[:,[0,2]], functions_y_0, eps, ['(x*,z*)', 'f(x,y*,z)', 'x', 'z'])
    draw_newton_method_3d(log[:,1:], functions_x_0, eps, ['(y*,z*)', 'f(x*,y,z)', 'y', 'z'])