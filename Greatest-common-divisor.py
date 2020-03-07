def gcd(a, b):
    #FIXME: IMPLEMENT THIS METHOD
    while(b != 0):#while the remainder is not zero
        
        m=a//b#(a div b)
        
        a1=a#update the subtractor variable
        
        a=b#update the variable being subtracted
        
        b=a1-m*b#the Eulerian algorithm
        
    return a#return the result

