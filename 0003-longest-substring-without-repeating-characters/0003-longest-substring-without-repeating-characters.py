class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett = set()
        max_len = 0
        left = 0
        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            max_len = max(max_len, right-left+1)
        return max_len