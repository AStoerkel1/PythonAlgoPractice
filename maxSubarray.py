#Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum
#found the algorithm on G4G kicking myself that i didn't think of it
def maxSubarray(nums: list) -> int:
    total = -10**4 - 1
    running_total = 0

    for x in nums:
        running_total = running_total + x
        if total < running_total:
            total = running_total
        if running_total < 0:
            running_total = 0
    return total

print(maxSubarray([-2, -3, 4, -1, -2, 1, 5, -3]))