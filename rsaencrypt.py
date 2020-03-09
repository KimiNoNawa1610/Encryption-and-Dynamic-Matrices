def encryptRSA(m, p, q, e):
    """encrypts the plaintext m, using RSA and the key (p * q, e)
    INPUT:  m - plaintext as a string of letters
            p, q - prime numbers used as part of the key n = p * q to encrypt the ciphertext
            e - integer satisfying gcd((p-1)*(q-1), e) = 1
            
    OUTPUT: The encrypted message as a string of digits
    """
    pass


def blocksize(n):
    """returns the size of a block in an RSA encrypted string"""
    twofive = "25"
    while int(twofive) < n:
        twofive += "25"
    return len(twofive) - 2
