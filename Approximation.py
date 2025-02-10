import math
import matplotlib.pyplot as plt
import numpy as np

delta = 0.001
x1,y1=0,10
n1 = 1
n2 = 1.33
x2,y2=map(int, input().split(' '))
def f(x):
    return n1*math.sqrt(x**2+y1**2) + n2*math.sqrt((x2-x)**2+y2**2)
def get_min(from_, to_, func):
    answer = -1
    answer_x = 0
    i=from_ #present number
    global delta #Step
    while i<to_:
        # print(func(i))
        if func(i)<answer or answer == -1: #It will be true, if "y" has different signs, or one of them equals 0
            answer=func(i)
            answer_x = i
        i+=delta
        # print("Present i:", i, "From:", from_, answers)
    x = np.linspace(0, x2, 100)  # 100 точек от -10 до 10
    ya = n1*np.sqrt(x**2+y1**2) + n2*np.sqrt((x2-x)**2+y2**2)
    # Построение графиков
    plt.plot(x, ya, label="x**3-x+1", color="blue")

    # Настройка
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()
    return round(answer_x, 5)

print(get_min(0, x2, f))

