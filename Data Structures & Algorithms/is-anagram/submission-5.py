class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if not same length then not anagram
        if len(s) != len(t):
            return False
        let_dict = {}
        for let in s:
            if let not in t:
                return False
            if let in let_dict:
                let_dict[let] += 1
            else:
                let_dict[let] = 1
        
        let_dict_two = {}
        for let in t:
            if let in let_dict_two:
                let_dict_two[let] += 1
            else:
                let_dict_two[let] = 1

        anagram = True
        bigger_word = t
        if len(s) > len(t):
            bigger_word = s
        for let in bigger_word:
            if let_dict[let] != let_dict_two[let]:
                anagram = False
        return anagram
