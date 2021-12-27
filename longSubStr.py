def longestSubString(s: str):
    subStr = ""
    temp = ""
    
    for i in s:
        if temp + i in s and i not in temp:
            temp = temp+i
        else:
            temp = i
        if len(temp) > len(subStr):
            subStr = temp
        
    return len(subStr)


'''
i think this need to be solved with a nested loop but I'm not sure right now
'''

'''
s="abcabcbb"
s="pwwkew"
s="bbbb"
'''
s = "dvdf"
print(longestSubString(s))