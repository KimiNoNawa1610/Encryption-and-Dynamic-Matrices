from plotting import plot
def scale(s,k):
    T=[]
    if(k <=0 ):
        raise ValueError ("k needs to be positive float")
    else:
        for z in S:
            h = complex(z.real * k,z.imag * k)
            T.append(h)
        return T
pass

S = {2 + 2j, 3 + 2j , 1.75 + 1j, 2 + 1j, 2.25 + 1j, 2.5 + 1j, 2.75 + 1j, 3 + 1j, 3.25 + 1j}

U = scale(S, 3)
plot(S)
plot(U,11)
