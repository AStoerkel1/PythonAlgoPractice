#find the first invalid number with the 
#least number of calls to isBadVersion()

#not working

def isBadVersion(x) -> bool:
    return x > 5

def firstBadVersion(n: int) -> int:
    min = 1
    max = n
    mid = n//2
    while min <= max:
        mid = (max + min) // 2
        if min >= max:
            return mid
        elif not isBadVersion(mid):
            max = mid + 1
            print("+")
        else:
            min = mid - 1
            print("-")

    return mid

print(firstBadVersion(8))