from math import sin
import math 

#台形積分の関数
def trapezoidal (f, a=0, b=1, n=100):
    h=(b-a)/n
    total=0
    for x in range (n):
        top=(f(a+x*h))
        bottom=(f(a+(x+1)*h))
        total+=((top+bottom)*h/2)
    return total



#(1) 
print(trapezoidal(f=math.sin, a=0, b=math.pi/2, n=50))

#(2)
def func_A(x):
    return 4/(1+x**2)
print(trapezoidal(f=func_A, a=0, b=1 ,n=100))

#(3)
def func_B(x):
    return math.sqrt(math.pi)*math.exp(-x**2)
print(trapezoidal(f=func_B, a=-100, b=100, n=1000))

