import math
delta = 0.01*2 #Step*2
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
            answers.append(i+delta/2) #As result, we have answer +- delta/2
            # print(answers)
        i+=delta
        # print("Present i:", i, "From:", from_, answers)
    return answers
print(*get_answer(-1000,1000,equation1))
print(*get_answer(-1000,1000,equation2))
print(*get_answer(-1000,100,equation3))
print(*get_answer(1,1000,equation4))
print(*get_answer(-1000,1000,equation5))
