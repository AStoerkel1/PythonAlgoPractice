#find the first invalid number with the 
#least number of calls to isBadVersion()


#first bad version is 6
def isBadVersion(x) -> bool:
    return x > 5

def firstBadVersion(n: int) -> int:
    min = 1
    max = n
    mid = n//2
    while min <= max:
        mid = (min + max) // 2
        if min == max:
            if not isBadVersion(mid):
                return mid + 1
            else:
                return mid 
        if isBadVersion(mid):
            print("-1")
            max = mid - 1
        else:
            print("+1")
            min = mid + 1


print(firstBadVersion(12))