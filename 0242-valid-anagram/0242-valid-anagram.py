class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        isAnagram = True
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in my_dict:
                    my_dict[s[i]] += 1
                else:
                    my_dict[s[i]] = 1
            
            for j in range(len(t)):
                if t[j] in my_dict:
                    my_dict[t[j]] -= 1
                else:
                    isAnagram = False
                    break
            
            for v in my_dict.values():
                if v != 0:
                    isAnagram = False
                    break
        
        return isAnagram