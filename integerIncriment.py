def plusOne(l: list) -> list:
    val = len(l)-1
    while l[val] == 9:
        l[val]=0
        if val == 0:
            return [1] + l
        val-=1
    l[val]+=1
    return l

print(plusOne([9,9]))

