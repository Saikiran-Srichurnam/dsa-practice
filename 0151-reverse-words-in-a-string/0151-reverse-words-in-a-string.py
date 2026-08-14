class Solution:
    def reverseWords(self, s: str) -> str:
        my_list = []
        word = ""

        i, j = 0, 0
        while j < len(s) :
            if s[j].isalnum():
                word += s[j]
            elif s[j] == " " and len(word) > 0:
                my_list.insert(0, word)
                word = ""
                i = j
            
            j += 1

        my_list.insert(0, word)
        return " ".join(my_list).strip()
        
        