class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a, b = 0, 0
        s = ""
        while a < len(word1) and b < len(word2):
            if a == b:
                s += word1[a]
                a += 1
            else: 
                s += word2[b]
                b += 1
            

        
        # check if any pointers are still within their words and take those slices
        if a < len(word1):

            return s + word1[a:]
        elif b <len(word2):
            return s + word2[b:]
        
        return s