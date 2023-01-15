def isHappy(n):
    '''
    A happy number is a number defined by the 
    following process:
    Starting with any positive integer, replace 
    the number by the sum of the squares of its 
    digits. Repeat the process until the number 
    equals 1 (where it will stay), or it loops 
    endlessly in a cycle which does not include 1.
    Those numbers for which this process ends 
    in 1 are happy.
    '''
    global s
    k = 0 
    while k<=10:
        digits = str(n)
        s = 0
        for d in digits:
            s = s + int(d)**2
        n = str(s)
        k += 1
    return s == 1