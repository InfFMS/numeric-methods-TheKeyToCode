import math
import matplotlib.pyplot as plt
import numpy as np
delta = 0.01 #Step*2
e = 2.71 #We don't use math.e because it's too many numbers after point.

def equation1(x):
    return math.cos(x)
def equation2(x):
    return math.cos(x)+0.1*x**2
def equation3(x):
    return -math.tanh(x-math.pi/2)
def equation4(x):
    return -0.2*(x-math.pi)**3 + 0.5*(x-math.pi)**2 + 1

def get_length(from_, to_, func):
    i=from_ #present number
    length = 0
    global delta #Step
    while i+delta<to_:
        length += math.sqrt(delta**2+(func(i) - func(i+delta))**2)
        i+=delta
        # print("Present i:", i, "From:", from_, answers)
    return round(length,4)
def write_graphics():
    # Данные
    x = np.linspace(0, 12, 100)  # 100 точек от -10 до 10
    y1 = np.cos(x)
    y2 = np.cos(x)+0.1*x**2
    y3 = -np.tanh(x-np.pi/2)
    y4 = -0.2*(x-np.pi)**3 + 0.5*(x-np.pi)**2 + 1
    # Построение графиков
    plt.plot(x, y1, label="cos(x)", color="blue")
    plt.plot(x, y2, label="cos(x)+0.1*x^2", color="green")
    plt.plot(x, y3, label="-tanh(x-Pi/2)", color="red")
    plt.plot(x, y4, label="-0.2*(x-Pi)^3 + 0.5*(x-Pi)^2+1", color="yellow")

    # Настройка
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()
write_graphics()

print(get_length(0, math.pi, equation1))
print(get_length(0, math.pi, equation2))
print(get_length(0, math.pi, equation3))
print(get_length(0, math.pi, equation4))
