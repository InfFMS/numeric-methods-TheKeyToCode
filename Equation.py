import math
import matplotlib.pyplot as plt
import numpy as np


delta = 0.01 #Step*2
e = 2.71 #We don't use math.e because it's too many numbers after point.
#Equathins
def equation1(x):
    return x**3-x+1
def equation2(x):
    return x**3-x**2-9*x+9
def equation3(x):
    return x**2-e**x
def equation4(x):
    return 5*x-6*math.log(x,e)-7
def equation5(x):
    return math.cos(x)+2*x-3

#This function will find answers
def get_answer(from_, to_, func):
    answers = []
    i=from_ #present number
    global delta #Step
    while i<to_:
        if func(i)*func(i+delta)<=0: #It will be true, if "y" has different signs, or one of them equals 0
            answers.append(round(i+delta/2,2)) #As result, we have answer +- delta/2
            # print(answers)
        i+=delta
        # print("Present i:", i, "From:", from_, answers)
    return answers
def write_graphics():
    # Данные
    x = np.linspace(-1, 5, 100)  # 100 точек от -10 до 10
    y1 = x**3-x+1
    y2 = x**3-x**2-9*x+9
    y3 = x**2-e**x
    y4 = 5*x-6*np.log(x)-7
    y5 = np.cos(x)+2*x-3
    # Построение графиков
    plt.plot(x, y1, label="x**3-x+1", color="blue")
    plt.plot(x, y2, label="x**3-x**2-9*x+9", color="green")
    plt.plot(x, y3, label="x**2-e**x", color="red")
    plt.plot(x, y4, label="5*x-6*math.log(x,e)-7", color="yellow")
    plt.plot(x, y5, label="math.cos(x)+2*x-3", color="purple")

    # Настройка
    plt.title("Графики sin(x) и cos(x)")
    plt.xlabel("Значения X")
    plt.ylabel("Значения Y")
    plt.legend()
    plt.grid(True)  # Сетка на графике
    plt.show()

write_graphics()
print(*get_answer(-1000,1000,equation1))
print(*get_answer(-1000,1000,equation2))
print(*get_answer(-1000,100,equation3))
print(*get_answer(1,1000,equation4))
print(*get_answer(-1000,1000,equation5))
