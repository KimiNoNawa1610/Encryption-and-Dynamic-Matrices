def modExp(b, n, m):
    binary=""
    output=1
    power=1
    while n > 0:
        binary=str(n%2)+binary
        n=int(n/2)
    power=b
    for i in binary[::-1]:
        if(i=="1"):
            output=(output*power)%m
        power=(power*power)%m
        print("Power: ",power,"i: ",i,"output :",output)
    return output
print(modExp(25,2525,77))
