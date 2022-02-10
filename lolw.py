def lengthOfLastWord(s: str) -> int:
    return len(s.split()[-1])

print(lengthOfLastWord("this         that   the   other "))