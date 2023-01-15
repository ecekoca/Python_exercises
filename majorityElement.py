def majorityElement(nums):
    '''
    The majority element is the element that 
    appears more than ⌊n / 2⌋ times. You may 
    assume that the majority element always 
    exists in the array.
    Given an array nums of size n, return the 
    majority element.
    '''
    nums = sorted(nums)
    k = int(len(nums)/2)
    return nums[k]