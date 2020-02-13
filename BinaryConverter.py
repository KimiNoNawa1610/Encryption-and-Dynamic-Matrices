# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def binaryAdd(a, b): #This is the beginning of a Python function
    """ This is the function's docstring
    returns the sum of two binary numbers a and b
    INPUT: a,b - string representation of the binary numbers
    OUPUT: string representation of their sum
    """
    a = a.replace(" ", "") #removing all whitespaces in string a
    b = b.replace(" ", "") #removing all whitespaces in string b
    #FIXME: REMOVE ALL WHITESPACES IN STRING b
    
    m = len(a) #number of digits in string a
    n = len(b) #number of digits in string b
    
    if m < n: #if string a is shorter than string b
        num_missing_zeros = n - m
        a = num_missing_zeros*"0" + a #appending 0's to the beginning of string a, to make it the same length as b
    
    #FIXME: IF STRING b IS SHORTER THAN STRING a, APPEND 0's TO THE BEGINNING OF STRING b TO MAKE LENGTHS EQUAL
    if n<m:
        num_missing_zeros_b=m-n
        b=num_missing_zeros_b*"0"+b
    
    #FIXME: FINISH THE FUNCTION SO THAT IT RETURNS THE DESIRED OUTPUT 
    c="0" #the carry digits
    output=""#the result
    
    for i in range(m-1,-1,-1):#start from the right hand side of the binary string
        output=str((int(c[0])+int(a[i])+int(b[i]))%2)+output#increment the result
        c=str((int(c[0])+int(a[i])+int(b[i]))//2)+c#increment the carry
    if(c[0]=="1"):#If the carry is overflowed
        output="1"+output# add "1" in front of the result
   
    return output
    
        
print(binaryAdd("01111","11011"))
        
        
          
        
        
            
            
            
            
    
