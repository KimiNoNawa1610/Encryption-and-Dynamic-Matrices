def modExp(b, n, m):
    binary=""#the power of the number in binary 
    output=1#initialize the output
    power=1#Initial value of output
    while n > 0:#The while loop
        binary=str(n%2)+binary
        n=int(n/2)
    power=b
    for i in binary[::-1]:#iterate the binary string from right to left
        if(i=="1"):
            output=(output*power)%m
        power=(power*power)%m
        print("Power: ",power,"i: ",i,"output :",output)
    return output

