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
        
        b=a1-m*b#the eulerian algorithm
        
        sn=s1-m*sn#sn=sn-2-sn-1(a div b)
        
        tn=t1-m*tn#tn=(tn-2)-(tn-1)(a div b)
        
    return(s, t)#return the bezout coefficients
