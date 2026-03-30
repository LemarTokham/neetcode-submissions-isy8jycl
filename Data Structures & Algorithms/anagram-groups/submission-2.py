class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_anagram(a,b):
            return sorted(a) == sorted(b)


        # check for multiple anagrams
        results = []
        for i in range(len(strs)):
            word_a = strs[i]
            # check if current word is already in our list, if so, skip iteration
            word_in_list = False
            for l in results:
                if word_a in l:
                    word_in_list = True
            if word_in_list:
                continue
            
            # initiate our anagram list ready to contain matches
            anagram = [word_a] 
            
            for j in range(i + 1, len(strs)): # compare our current word with every subsequent word for anagram match
                word_b = strs[j]
                if check_anagram(word_a, word_b):
                    anagram.append(word_b)
            results.append(anagram)
        return results

        