class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for i in range(len(s)):
            if s[i] in s_map and t[i] in t_map:
                s_map[s[i]].append(i)
                t_map[t[i]].append(i)
            else:
                s_map[s[i]] = [i]
                t_map[t[i]] = [i]

        for sval, tval in zip(s_map.values(),t_map.values()):
            if sval != tval:
                return False

        return True