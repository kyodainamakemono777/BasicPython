from math import sin
import math 


#aとbの値
a=0
b=(1/2)*math.pi



#aからbの区間をn等分してhを求める （台形の高さ）
n=100
h=(b-a)/n




#f(a)からf(b)までの100個のsin関数を当てはめた値を求める　　f(0),f(1),f(2),.....f(100) 　そして100個リストに格納しました
sin_values=[]
for x in range(n+1):
    split_point=a+(x*h)
    sin_values.append(sin(split_point))




#求めた間数値で小さい台形の面積を100個求める そして面積リストに追加しました（100個分の台形の面積の値が格納されてます）
area_list=[]
for i in range(n):
    top=(sin_values[i])
    bottom=(sin_values[i+1])
    area=((top+bottom)*h)/2
    area_list.append(area)


#100個の台形の面積を全部足し合わせる  近似しました！
total=sum(area_list)
print(total)