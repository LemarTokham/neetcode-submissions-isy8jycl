class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def check_anagram(a,b):
            # check for same length
            if len(a) != len(b):
                return False
            # add both to hashmap
            dict_a = {}
            dict_b = {}
            # if they are already the same length i can just make both hashmaps in the same loop
            for i in range(len(a)):
                let_a = a[i]
                let_b = b[i]
                # check if letter is already in dict_a
                if let_a not in dict_a:
                    dict_a[let_a] = 1 # if not, add it in with a count of # -*- coding: latin-1 -*-
                else:
                    dict_a[let_a] += 1 # if it's already in there, we have seen it again and therefore increase its count
                
                # check if letter is already in dict_b
                if let_b not in dict_b:
                    dict_b[let_b] = 1 # if not, add it in with a count of # -*- coding: latin-1 -*-
                else:
                    dict_b[let_b] += 1 # if it's already in there, we have seen it again and therefore increase its count
            for j in range(len(a)):
                # check both for same letters
                # we are comparing the letters in 'a' to see if they are in 'b'
                current_let = a[j]
                if current_let not in dict_b:
                    return False # if letter in word a is not in word b, then not an anagram
                if dict_a[current_let] != dict_b[current_let]:
                    return False
            return True
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

        