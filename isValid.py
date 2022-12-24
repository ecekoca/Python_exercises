def isValid(s):
    opens=['(','[','{']
    closes=[')',']','}']
    stack = []
    for p in range(len(s)):
        if s[p] in opens:
            stack.append(s[p])
        elif s[p] in closes:
            if stack == []:
                return False
            elif opens.index(stack[-1])==closes.index(s[p]):
                stack = stack[:-1]
            else:
                return False
    if stack==[]:
        return True
    else:
        return False

isValid("(){}}{")