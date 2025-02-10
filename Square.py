import math
delta = 0.01

def top1(x):
    return math.sin(2*x)+1
def bottom1(x):
    return -0.2*x**2+0.5

def top2(x):
    return math.cos(x)+1.2
def bottom2(x):
    return -0.5*x**2+0.7

def top3(x):
    return math.e**(-(x)**2) + 1
def bottom3(x):
    return -0.3*x**3+0.5

def top4(x):
    return math.e**(-(x**2)) + 0.5
def bottom4(x):
    return 0.2*math.sin(3*x)-0.5

def top5(x):
    return math.e**(-(x+1)**2) + math.e**(-(x-1)**2) + 0.5
def bottom5(x):
    return -0.3*x**2

def find_square(from_, to_, bottom, top):
    i = from_
    square = 0
    while i+delta<to_:
        l1 = abs(top(i)-bottom(i))
        l2 = abs(top(i+delta)-bottom(i+delta))
        delta_square = (l1+l2)/2*delta
        square+=delta_square
        i+=delta
    return round(square,3)

print(find_square(0, math.pi, bottom1, top1))
print(find_square(-math.pi/2, math.pi/2, bottom2, top2))
print(find_square(-2, 2, bottom3, top3))
print(find_square(-2, 2, bottom4, top4))
print(find_square(-2, 2, bottom5, top5))
