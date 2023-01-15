def pascalsTriangle(numRows):
    '''
    Given an integer numRows, return 
    the first numRows of Pascal's triangle.
    '''
    p = []
    for r in range(numRows):
        if r==0:
            row = [1]
        elif r==1:
            row = [1,1]
        else:
            row = []
            for idx,val in enumerate(p[r-1]):
                if idx != len(p[r-1])-1:
                    row.append(val+p[r-1][idx+1])
            row.insert(0,1)
            row.append(1)
        p.append(row)
    return p