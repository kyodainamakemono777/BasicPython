#二次方程式の解を返す関数

def calc(a,b,c,):
    x=(-b+(((b**2)-4*a*c)**0.5))*(1/(2*a))           #解一つ目をxに代入
    y=(-b-(((b**2)-4*a*c)**0.5))*(1/(2*a))           #解二つ目をyに代入
    return x,y                               


#⑴
a=1
b=-6
c=9
x1,x2=calc(a,b,c)
print(x1,x2)

#(2)
a=1
b=2
c=-8
x1,x2=calc(a,b,c)
print(x1,x2)

#(3)
a=8
b=-6
c=-35
x1,x2=calc(a,b,c)
print(x1,x2)

#(4)修正しました
a=1
b=0
c=1
x1,x2=calc(a,b,c)
print(x1,x2)

