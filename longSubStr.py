def longestSubString(s: str):
    subStr = ""
    temp = ""
    #loop through the string
    for  i in s:
        #if the char isn't already in the temp string then append
        if i not in temp:
            temp = temp+i
        else:
            #if it is, then find its first occurance in temp
            #and start the new temp from +1 index higher
            temp = temp[temp.find(i)+1:]+ i
        if len(temp) > len(subStr):
            subStr = temp
    return len(subStr)

'''
s="abcabcbb"
s="pwwkew"
s="bbbb"
'''
s = "aabaab!bb"
print(longestSubString(s))