def sum_proper_divisors(n):
    return 1+sum([i+n//i if i!=n/i else i for i in range(2,int(n**0.5+1)) if n%i==0])
print(sum_proper_divisors(100))
