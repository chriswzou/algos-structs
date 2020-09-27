# 138. Word Break 
# Given a non-empty string and a dictionary of non-empty words,
# determine if the string can be broken down into those words.

# Key insight: use an i and a j to split the current string
# under consideration into two halves. The string is valid if
# you've checked the first half and the second half is in words.

def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    dp = [False] * (len(s) + 1)
    wordDict = set(wordDict)
    for i in range(len(s) + 1):
        if i == 0:
            dp[i] = True
        for j in range(i):
            if s[j:i] in wordDict and dp[j]:
                dp[i] = True
    print(dp)
    return dp[-1]
