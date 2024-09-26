from math import sin
import math 

#台形積分の関数
def trapezoidal (f, a=0, b=1, n=100):
    h=(b-a)/n
    values=[]
    for x in range (n+1):
        values.append(f(a+(x*h)))
    
    area_list=[]
    for y in range (n):
        top=values[y]
        bottom=values[y+1]
        area_list.append((top+bottom)*h/2)
    
    total=sum(area_list)
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
