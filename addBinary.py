def addBinary(a, b):
    '''
    Given two binary strings a and b, return their 
    sum as a binary string.
    '''
    
    int_sum = 0
    for s,i in zip(str(a), reversed(range(len(str(a))))):
        int_sum = int_sum + int(s)*(2**i)
    for s,i in zip(str(b), reversed(range(len(str(b))))):
        int_sum = int_sum + int(s)*(2**i)
    return bin(int_sum)[2:]