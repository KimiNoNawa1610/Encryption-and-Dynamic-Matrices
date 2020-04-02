from plotting import plot
def translate(S, z0):
    """
    translates the complex numbers of set S by z0
    INPUT: 
        * S - set of complex numbers
        * z0 - complex number
    OUT:
        * T - set consisting of points in S translated by z0
    """
    #FIXME: IMPLEMENT FUNCTION
    output=set()
    for i in S:
        n=i+z0
        output.add(n)
    return output
    pass

