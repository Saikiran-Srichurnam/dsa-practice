class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        counter = 1
        i = 0
        j = 1
        while j < len(s):
            if s[j] not in s[i:j]:
                j += 1
                counter = max(counter, j - i)
            else:
                i += 1
        
        return counter
