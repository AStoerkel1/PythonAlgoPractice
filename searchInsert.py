#does a binary search for the target
#if the target is not found then it's proper index is returned
def searchInsert(nums: list, target: int) -> int:
    if target < nums[0]: return 0
    if target > nums[-1]: return len(nums)

    min = 0
    max = len(nums)-1
    while min<=max:
        mid = (max + min)//2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            min = mid + 1
        if target < nums[mid]:
            max = mid - 1
    if nums[mid] < target:
        return mid + 1
    else:
        return mid

        
    

print(searchInsert([1,2,3,4,6], 5))
