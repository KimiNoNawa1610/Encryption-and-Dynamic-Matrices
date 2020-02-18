def modExp(b, n, m):
    #FIXME: IMPLEMENT THIS METHOD
    binary=""#initialize the exponent of the number in binary form
    output=1#initialize the result
    power=b#The original power is the number (b)
    while(n > 0):#if n is not zero
        binary=str(n%2)+binary#convert the exponent to binary
        n=int(n/2)
        for i in binary[::-1]:#interate through the binary exponent from right to left
        if(i=="1"):#if binary exponent component is not zero
            output=(output*power)%m#update the result 
        power=(power*power)%m#double the number (b)
    return output#return the output
