def longestSubString(s: str):
    subStr = ""
    temp = ""
    for  i in s:
        if i not in temp:
            temp = temp+i
        else:
            temp = temp[temp.find(i)+1:]+ i
            #print(temp)
        if len(temp) > len(subStr):
            subStr = temp
            print(subStr)
    return len(subStr)

'''
s="abcabcbb"
s="pwwkew"
s="bbbb"
'''
s = "aabaab!bb"
print(longestSubString(s))