#最大公約数を求める関数
def find_gcd(a,b):
    if a<b:
        a,b=b,a

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
find_gcd(629,259)


#10と20の最大公約数
find_gcd(10,20)

#14と91の最大公約数
find_gcd(14,91)

#91と14の最大公約数
find_gcd(91,14)


#input関数を使ったやりかたでも最大公約数を求めることができるようにしました
a_1=int(input("aの値を入力してください"))
b_1=int(input("bの値を入力してください"))
a,b=a_1,b_1
print(a_1,"と",b_1,"の",end=' ')
find_gcd(a,b)