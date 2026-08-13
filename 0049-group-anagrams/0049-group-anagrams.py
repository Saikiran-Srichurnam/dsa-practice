class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grp_anagrams = {}

        for word in strs:
            sorted_wrd = "".join(sorted(word))
            if sorted_wrd in grp_anagrams:
                grp_anagrams[sorted_wrd].append(word)
            else:
                grp_anagrams[sorted_wrd] = [word]
            
        return list(grp_anagrams.values())