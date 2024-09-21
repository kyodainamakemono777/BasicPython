#大小関係を判定した後、最大公約数を求めています


# 【大小判定】２つの値のどちらが大きいか小さいか判定しています　
def max_min(x,y):
    if x>y or x==y:
        a,b=x,y
        return a,b
    elif x<y:
        a,b=y,x
        return a,b


#最大公約数を求める関数
def find_gcd(a,b):
    r=a%b
    if r==0:
        print("最大公約数は",b)
    else:
        while True:
            a=b
            b=r
            r=(a%b)
            if r==0:
                print("最大公約数は",b)
                break


#一度で割り切れて、余りが0になったら、その数が最大公約数になります
#一度で割り切れないものは、余りが0になるまで割るのを繰り返します



#test　629と259の最大公約数
a,b=max_min(629,259)
find_gcd(a,b)


#10と20の最大公約数
a,b=max_min(10,20)
find_gcd(a,b)

#14と91の最大公約数
a,b=max_min(14,91)
find_gcd(a,b)

#91と14の最大公約数
a,b=max_min(91,14)
find_gcd(a,b)


#input関数を使ったやりかたでも最大公約数を求めることができるようにしました
a_1=int(input("aの値を入力してください"))
b_1=int(input("bの値を入力してください"))
a,b=a_1,b_1
a,b=max_min(a,b)
print(a_1,"と",b_1,"の",end=' ')
find_gcd(a,b)


