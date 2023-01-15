def twoSum(nums,target):
    '''
    Given an array of integers nums and an 
    integer target, return indices of the 
    two numbers such that they add up to target.
    '''
    seen = {}
    for idx,val in enumerate(nums):
        rem = target - val
        if rem not in seen:
            seen[val] = idx
        else:
            return [seen[rem], idx]