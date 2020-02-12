def gcd(a, b):
    m=0
    divisor=0
    if a<=b:
        m=a
    elif a>b:
        m=b
    i=1
    while i<=m:
        if a%i==0 and b%i==0:
            divisor=i
        i=i+1
    return divisor
print(gcd(414,662 ))
