def romanToInt(s):
    keys = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    n = 0

    for i in range(len(s)):
        n = n + keys[s[i]]
        if i !=0:
            if s[i-1]=='I' and s[i]=='V':
                n = n - 2
            elif s[i-1]=='I' and s[i]=='X':
                n = n - 2
            elif s[i-1]=='X' and s[i]=='L':
                n = n - 20 
            elif s[i-1]=='X' and s[i]=='C':
                n = n - 20      
            elif s[i-1]=='C' and s[i]=='D':
                n = n - 200
            elif s[i-1]=='C' and s[i]=='M':
                n = n - 200  
    return n

romanToInt('MCMXCIV')