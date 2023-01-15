def singleNumber(nums):
    '''
    Given a non-empty array of integers 
    nums, every element appears twice 
    except for one. Find that single one.
    '''
    count = {}
    for d in nums:
        if d not in count:
            count[d] = 1
        else:
            count[d] += 1
    sgl = [i for i in count.keys() if count[i]==1]
    return sgl[0]