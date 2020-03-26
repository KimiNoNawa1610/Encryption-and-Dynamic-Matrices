def rotate(S, theta):
    """
    rotates the complex numbers of set S by theta radians.  
    INPUT: 
        * S - set of complex numbers
        * theta - float. If negative, the rotation is clockwise. If positive the rotation is counterclockwise. If zero, no rotation.
    OUT:
        * T - set consisting of points in S rotated by theta radians
        
    """
    #FIXME: IMPLEMENT FUNCTION
    sim=set()
    if(theta==0):
        return S
    elif(theta>0):
        for i in S:
            n=complex(i.replace("j",""))
            sim.add(n)
            
        print(sim)

    pass

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}
rotate(S, 1)
