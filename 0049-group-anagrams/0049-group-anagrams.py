class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in grp_anagrams:
                grp_anagrams[sorted_word].append(word)
            else:
                grp_anagrams[sorted_word] = [word]
            
        return list(grp_anagrams.values())

