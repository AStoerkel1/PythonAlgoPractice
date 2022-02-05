#don't use find
def strStr( haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    
    for x in range(len(haystack)):
        if haystack[x:len(needle)+x] == needle:
            return x
    return -1

print(strStr("llllllldlll", "ld"))
