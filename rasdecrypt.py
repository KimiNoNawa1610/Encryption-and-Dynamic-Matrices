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

def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
