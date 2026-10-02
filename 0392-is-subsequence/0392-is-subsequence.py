class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res = ""
        isValid = False
        i = 0
        j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                res += s[j] 
                j += 1
            i += 1
        
        if res == s:
            isValid = True
        
        return isValid