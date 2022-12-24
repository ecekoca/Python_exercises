def isPalindrome(x):
    num = str(x)
    rev_num = num[::-1]
    if num==rev_num:
        return True
    else:
        return False