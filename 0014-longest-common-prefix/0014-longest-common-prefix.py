class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            i = 0

            while i < len(prefix) and i < len(word):
                if prefix[i] != word[i]:
                    break
                
                i += 1
            
            prefix = prefix[:i]

        return prefix

