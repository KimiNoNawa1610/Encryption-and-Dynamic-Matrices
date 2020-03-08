def modinv(a,m):
    """returns the inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: a inverse as an integer
    """
    c=m
    s=1
    t=0
    sn=0
    tn=1
    while(m!=0):
        b=a//m
        a1=a
        a=m
        s1=s
        s=sn
        t1=t
        t=tn
        m=a1-b*m
        sn=s1-b*sn
        tn=t1-b*tn
    if(a!=1):
        
        return "The given values are not relatively prime"
    
    else:
        
        while(s<0):
            s=s+c
        while(s>c):
            s=s-c
        return s 
    return 0

print(modinv(18,19))

