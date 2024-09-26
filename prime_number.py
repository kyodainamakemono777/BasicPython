#素数判定の関数  
def is_prime(n):
    if "." in n:
        return ("エラー　小数点を含まない数を入力してください")
    else:
        n=int(n)
        if n<1:
            return ("エラー　０より大きい数を入力してください")

    list=[1]
    for i in range(2,n+1):
        if n%i==0:
            list.append(i)
    
    if len(list)==2:
        return True
    else:
        return False


a = input("aの値を入力: ")
result_a=is_prime(a)
print(result_a)



#少数点を含む数や、負の数を入力するとエラーのメッセージが出るようにしました。
#素数であればTrue 素数じゃなければFalse がでます