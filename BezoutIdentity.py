def bezoutCoeffs(a, b):
    #FIXME: IMPLEMENT THIS METHOD.
    s=1#initialize the first case of the first bezout coefficient
    t=0#initialize the first case of the second bezout coefficient
    sn=0#initialize the n case of the first bezout coefficient
    tn=1#initialize the n case of the second bezout coefficient
    while(b != 0):#while the remainder is not zero
