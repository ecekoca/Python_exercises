def isIsomorphic(s, t):
    '''
    Two strings s and t are isomorphic if 
    the characters in s can be replaced to get t.
    '''
    d = {}
    k = 1
    s_n = []
    for ch in s:
        if ch not in d:
            d[ch] = k
            s_n.append(k)
            k += 1
        else:
            s_n.append(d[ch])

    d = {}
    k = 1
    t_n = []
    for ch in t:
        if ch not in d:
            d[ch] = k
            t_n.append(k)
            k += 1
        else:
            t_n.append(d[ch])

    return s_n == t_n