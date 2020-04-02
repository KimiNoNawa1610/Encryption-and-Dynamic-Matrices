import math
from plotting import plot
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
    
    output=set()
    if(theta==0):
        return S
    else:
        angle=complex(math.cos(theta),math.sin(theta))
        for i in S:
            n=i*angle
            output.add(n)
        return output
    pass





