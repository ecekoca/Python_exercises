def searchInsert(nums, target):
    '''
    Given a sorted array of distinct integers and
    a target value, return the index if the target 
    is found. If not, return the index where it 
    would be if it were inserted in order.
    '''
    
    idx = -1
    for i in range(len(nums)):
        if nums[i] == target and idx == -1:
            idx = i
        elif nums[i] > target and idx == -1:
            idx = i
    if target > nums[-1]:
        idx = len(nums)
    return idx