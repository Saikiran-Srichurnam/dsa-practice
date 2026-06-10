class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_list = {}
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                if s[i] in my_list:
                    my_list[s[i]] += 1
                else:
                    my_list[s[i]] = 1
            
            isAnagram = True
            for j in range(len(t)):
                if t[j] in my_list:
                    my_list[t[j]] -= 1
                else:
                    isAnagram = False
                    break
            
            for v in my_list.values():
                if v != 0:
                    isAnagram = False
                    break
        
        if isAnagram:
            return True
        else:
            return False