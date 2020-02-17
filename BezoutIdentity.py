def bezoutCoeffs(a, b):
    s=1
    t=0
    s1=0
    t1=1
    while(b!=0):
        m=a//b
        a1=a
        a=b
        sn=s
        s=s1
        tn=t
        t=t1
        b=a1-m*b
        s1=sn-m*s1
        t1=tn-m*t1
    return(s, t)
