def sum_proper_divisors1(n):
    result=1
    for i in range(2,int(n**0.5+1)):
        if n%i==0:
            result+=i+(n//i) if i != n//i else i
    return result


print(sum_proper_divisors1(100))