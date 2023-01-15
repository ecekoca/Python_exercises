def isTextPalindrome(s):
    '''
    A phrase is a palindrome if, after converting 
    all uppercase letters into lowercase letters 
    and removing all non-alphanumeric characters, 
    it reads the same forward and backward. 
    Alphanumeric characters include letters and 
    numbers.

    Given a string s, return true if it is a 
    palindrome, or false otherwise.
    '''
    s = s.lower().strip().replace(' ', '')
    for ch in s:
        if ch.isalpha()==False:
            s = s.replace(ch, '')
    return s == s[::-1]