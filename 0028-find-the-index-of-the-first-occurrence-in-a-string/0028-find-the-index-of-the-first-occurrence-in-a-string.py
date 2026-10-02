class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        i = 0
        j = 0
        k = 0
        while j < len(haystack) and k < len(needle):
            if haystack[j] == needle[k]:
                j += 1
                k += 1
            else:
                i += 1
                j = i
                k = 0  
                
        if k == len(needle):
            return i

        if j == len(haystack):
            return -1