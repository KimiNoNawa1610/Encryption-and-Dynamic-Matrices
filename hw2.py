#Nhan Vo
# ### Programming Tasks
# 
#
# ##### Utility functions (NO EDITS NECESSARY)

# In[31]:


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


# In[32]:

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


# In[ ]:


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2




# #### Problem 1: 
# Create a function `modinv(a,m)` that returns the inverse of `a` modulo `m`.  If the gcd of `a` and `m` is not 1, then you must `raise` a `ValueError` exception with message `"The given values are not relatively prime"`.  You can NOT use any built-in functions as part of your implementation, but you may import and use any functions you implemented for either Coded HW \#1 or Lab Assignment \#3.

# In[1]:


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


# #### Problem 2: 
# Create a function `affineEncrypt(text, a,b)` that returns the cipher text encrypted using key  (`a`, `b`).  You must verify that the gcd(a, 26) = 1 before making the encryption.  If this is not the case, the function must throw an `raise` a `ValueError` exception with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You can NOT use any built-in functions as part of your implementation, but you may import and use any functions you implemented for either Coded HW \#1 or Lab Assignment \#3.  You may also use the utility functions at the end of this notebook.

# In[ ]:


def affineEncrypt(text, a, b):
    """encrypts the plaintext 'text', using an affine transformation key (a, b)
    INPUT:  text - plaintext as a string of letters
            a - integer satisfying gcd(a, 26) = 1.  Raises error if such is not the case
            b - integer 
            
    OUTPUT: The encrypted message as a string of characters
    """
    c=26
    d=a
    while(c != 0):#while the remainder is not zero
        
        m=d//c#(a div c)
        
        a1=d#update the subtractor variable
        
        d=c#update the variable being subtracted
        
        c=a1-m*c#the Eulerian algorithm
    if(a!=1):
        return "The given key is invalid. The gcd(a,26) must be 1."
    else:
        output=""
        for i in text:
            p=int(letters2digits(i))
            encrypt=(a*p+b)%26
            digit=str(encrypt)
            if(len(digit)<2):
                digit="0"+digit 
            encryption=digits2letters(digit)
            output=output+encryption
            
        return output
    pass
    


# #### Problem 3: 
# Create a function `affineDecrypt(ciphertext, a,b)` that returns the cipher text encrypted using key  (`a`, `b`). You must verify that the gcd(a, 26) = 1.  If this is not the case, the function must `raise` a `ValueError` exception with message `"The given key is invalid. The gcd(a,26) must be 1."`.  You can NOT use any built-in functions as part of your implementation, but you may import and use any functions you implemented for either Coded HW \#1 or Lab Assignment \#3.  You may also use the utility functions at the end of this notebook. 

# In[ ]:


def affineDecrypt(ciphertext, a, b):
    """decrypts the string 'ciphertext', which was encrypted using an affine transformation key (a, b)
    INPUT:  ciphertext - a string of encrypted letters
            a - integer satisfying gcd(a, 26) = 1.  
            b - integer 
            
    OUTPUT: The decrypted message as a string of characters
    """
    c=26
    d=a
    while(c != 0):#while the remainder is not zero
        
        m=d//c#(a div c)
        
        a1=d#update the subtractor variable
        
        d=c#update the variable being subtracted
        
        c=a1-m*c#the Eulerian algorithm
    if(d!=1):
        return "The given key is invalid. The gcd(a,26) must be 1."
    else:
        decryption=""
        for i in ciphertext:
            compute=int(letters2digits(i))
            decrypt= str((modinv(a,26)*(compute-b))%26)
            if(len(decrypt)<2):
                decrypt="0"+decrypt
            decryption=decryption+digits2letters(str(decrypt))
            
        return decryption    
            
    pass


# #### Problem 4:
# 
# Implement the function `encryptRSA(m, p, q, e)` which encrypts a string `m` using RSA key `(n = p * q, e)`.  You can NOT use any built-in functions as part of your implementation, but you may import and use any functions you implemented for either Coded HW \#1 or Lab Assignment \#3.  You may also use the utility functions at the end of this notebook to aid you in your implementation. 

# In[1]:


def encryptRSA(m, p, q, e):
    """encrypts the plaintext m, using RSA and the key (p * q, e)
    INPUT:  m - plaintext as a string of letters
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    n=p*q
    size=blocksize(n)
  
    series=""
    for i in m:
        series=series+letters2digits(i)
    while (len(series)%size)!=0:
        series=series+"23"

    a=size
    b=0
    x=[]
    output=""
    y=""
    for i in range(size):
        x.append(series[b:a])
        b=a
        a=a+size
    for i in x:
        if(len(i)!=0):
            y=str((int(i)**e)%n)
            if(len(y)!=size):
                y="0"+y
            output=output+" "+y
    return output
    pass
    


# In[ ]:



# #### Problem 5:
# 
# Complete the implementation of the function `decryptRSA(c, p, q, m)` which depends on `modinv(a,m)` and the given functions `RSAdigits2letters(d)` and `blockSize(n)`.  When you are done, you can test your function against the given samples.

# In[ ]:


def decryptRSA(c, p, q, e):
    """decrypts the cipher c, which was encrypted using the key (p * q, e)
    INPUT:  c - ciphertext as a string of digits
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The decrypted message as a string of letters
    """
    
    decrypted=""
    original=""
    result=[]
    output=""
    code=c.split(" ")
    c=c.replace(" ", "")
    mod=abs((p-1)*(q-1))
    n=p*q
    inverse=modinv(e,mod)
    for i in code:
        decrypted=str((int(i)**inverse)%n)
        if(len(decrypted)!=len(i)):
            decrypted="0"+decrypted
        original=original+decrypted
    chunks = [original[i:i+2] for i in range(0, len(original), 2)]
    for i in chunks:
        output=output+digits2letters(i)
    return output
    pass








