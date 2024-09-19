
#2～自然数nまで順重に割っていく　　　　　n÷2, n÷3, n÷4, n÷5, n÷6....    n÷n　
# 1とnだけでしか割り切れないのであれば『素数』　それ以外は『素数じゃない』にしています


#素数判定の関数
def is_prime(n):
    list=[1]
    for i in range(2,n+1):
        if n%i==0:
            list.append(i)
    
    print("この数は{}で割り切れます".format(list))
    
    if len(list)==2:
        print("この数は素数です")
    else:
        print("この数は素数ではありません")


a = int(input("aの値を入力: "))
b = int(input("bの値を入力: "))

is_prime(a)
is_prime(b)
