def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2

def letters2digits(letters):
    """converts a string of letters A-Z to a string of double digits without spaces in the range 00-25"""
    letter2digit = {"A" : "00", "B" : "01", "C" : "02", "D" : "03", "E" : "04", 
                  "F" : "05", "G" : "06", "H" : "07", "I" : "08", "J" : "09",
                  "K" : "10", "L" : "11", "M" : "12", "N" : "13", "O" : "14",  
                  "P" : "15", "Q" : "16", "R" : "17", "S" : "18", "T" : "19",
                  "U" : "20", "V" : "21", "W" : "22", "X" : "23", "Y" : "24", 
                  "Z" : "25"}
        
    digits = ""  #initializing digits string
    letters = "".join(letters.split()) #removing whitespaces in the text

    
    for i in range(0, len(letters)):
        if(letters[i].isalpha()):
            letter = letters[i].upper()  #converting to uppercase
            digit = letter2digit[letter]
            digits += digit     # concatenating to the string of digits
    
    return digits

def encryptRSA(m, p, q, e):
    """encrypts the plaintext m, using RSA and the key (p * q, e)
    INPUT:  m - plaintext as a string of letters
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    n=p*q
    size=blocksize(n)
    print(size)
    series=""
    for i in m:
        series=series+letters2digits(i)
    while (len(series)%size)!=0:
        series=series+"23"
    print(series)
    a=size
    b=0
    x=[]
    output=""
    for i in range(size):
        x.append(series[b:a])
        b=a
        a=a+size
    print(x)
    for i in x:
        if(len(i)!=0):
            output=output+str((int(i)**e)%n)
    print(output)
    
    pass
encryptRSA("UPLOAD",53,61,17)
