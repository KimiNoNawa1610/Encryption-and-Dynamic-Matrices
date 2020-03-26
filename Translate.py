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

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

T = translate(S, -1+2j)

print(T)
plot(S)
plot(T)
