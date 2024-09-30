#素数判定の関数  
def is_prime(n):
    values=[1]
    for i in range(2,n+1):
        if n%i==0:
            values.append(i)
    
    if len(values)==2:
        return True
    else:
        return False


a = int(input("値を入力: "))
result_a=is_prime(a)
print(result_a)