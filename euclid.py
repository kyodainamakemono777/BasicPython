#最大公約数を求める関数
def find_gcd(a,b):
    if a<b:
        a,b=b,a

    r=a%b
    if r==0:
        return b
    else:
        while r!=0:
            a,b=b,r
            r=(a%b)
        return b


#上の関数を使用して、お互いが素であるか判定する関数
def is_coprime (a,b):
    return find_gcd(a,b)==1




#2つ値を入力して最大公約数を求める
a=int(input("aの値を入力してください"))
b=int(input("bの値を入力してください"))
result=find_gcd(a,b)
print(result)


#お互いが素であるかを確認する 素であればTrue 違うとFalse
print(is_coprime(a,b))
