def digits2letters(digits):
    """converts a string of double digits without spaces in the range 00-25 to a string of letters A-Z"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digit2letter = dict((v,k) for k,v in letter2digit.items())  #creating a dictionary with keys and values exchanged
        
    letters = ""
    start = 0  #initializing starting index of first digit
    for i in range(0, len(digits), 2):
        digit = digits[start : start + 2]  # accessing the double digit
        letters += digit2letter[digit]     # concatenating to the string of letters
        start += 2                         # updating the starting index for next digit
    
    return letters

def modinv(a,m):
    """returns the inverse of a modulo m
    INPUT: a - integer
           m - positive integer
    OUTPUT: a inverse as an integer
    """
    c=m
    s=1
    t=0
    sn=0
    tn=1
    while(m!=0):
        b=a//m
        a1=a
        a=m
        s1=s
        s=sn
        t1=t
        t=tn
        m=a1-b*m
        sn=s1-b*sn
        tn=t1-b*tn
    if(a!=1):
        
        return "The given values are not relatively prime"
    
    else:
        
        while(s<0):
            s=s+c
        while(s>c):
            s=s-c
        return s 
    return 0

def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    code=c.split(" ")
    mod=abs((p-1)*(q-1))
    n=p*q
    modinv(e,n)
    pass
