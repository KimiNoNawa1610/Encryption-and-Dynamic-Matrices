from plotting import plot
def scale(S, k):
    """
    scales the complex numbers of set S by k.  
    INPUT: 
        * S - set of complex numbers
        * k - positive float, raises ValueError if k <= 0
    OUT:
        * T - set consisting of points in S scaled by k
        
    """
    #FIXME: IMPLEMENT FUNCTION
    output=set()
    if(k<=0):
        raise ValueError
    else:
        for i in S:
            n=i*k
            output.add(n)
        return output
    pass

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

U = scale(S, 3)

print(U)
plot(S)
plot(U,11)
