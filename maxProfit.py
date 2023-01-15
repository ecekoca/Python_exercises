def maxProfit(prices):
    '''
    The cost of a stock on each day is given 
    in an array, find the max profit that you 
    can make by buying and selling in those days.
    '''
    max_pr = 0
    for idx,val in enumerate(prices):
        if idx==0:
            cur_min = val
        elif val > cur_min and (val-cur_min)>max_pr:
            max_pr = val - cur_min
        elif val < cur_min:
            cur_min = val
    return max_pr