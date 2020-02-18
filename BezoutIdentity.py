def bezoutCoeffs(a, b):
    #FIXME: IMPLEMENT THIS METHOD.
    s=1#initialize the first case of the first bezout coefficient
    t=0#initialize the first case of the second bezout coefficient
    sn=0#initialize the n case of the first bezout coefficient
    tn=1#initialize the n case of the second bezout coefficient
    while(b != 0):#while the remainder is not zero
        m=a//b#(a div b)
        a1=a#update the subtractor variable 
        a=b#update the variable being subtracted
        s1=s#update s1(sn-2)
        s=sn#update the initial first bezout coefficient
        t1=t#update t1(tn-2)
        t=tn#update the initial second bezout coefficient
