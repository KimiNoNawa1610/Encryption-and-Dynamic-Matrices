def reflectH(S, k):
    """
    reflects the complex numbers of set S about the horizontal line y = k.  
    INPUT: 
        * S - set of complex numbers
        * k - float
    OUT:
        * set consisting of points in S reflected about the line y = k.
        
    """
    output=set()
    for i in S:
        distance=abs(i.imag-k)
        if i.imag>k:
            newpoint=complex(i.real,i.imag-2*distance)
            output.add(newpoint)
        if i.imag<k:
            newpoint=complex(i.real,i.imag+2*distance)
            output.add(newpoint)
    return output
    pass
