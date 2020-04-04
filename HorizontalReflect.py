import image
def reflectV(S, h):
    import math
    """
    reflects the complex numbers of set S about the vertical line x = h.  
    INPUT: 
        * S - set of complex numbers
        * h - float
    OUT:
        * set consisting of points in S reflected about the line x = h.
        
    """
    output=set()
    for i in S:
        d=abs(i.real-h)
        if i.real>h:
            newpoint=i-2*d
            output.add(newpoint)
        if i.real<h:
            newpoint=i+2*d
            output.add(newpoint)
    return output
    pass



