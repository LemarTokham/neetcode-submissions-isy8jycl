class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def isAnagram(word1, word2):
            if len(word1) != len(word2):
                return False
            # Creating hashmaps for each word
            word1Dict = {}
            word2Dict = {}
            for i in range(len(word1)): # O(n)
                let = word1[i]
                word1Dict[let] = word1Dict.get(let, 0) + 1 # if key doesnt exist, init as 0, else increment
            for j in range(len(word2)):
                let = word2[j]
                word2Dict[let] = word2Dict.get(let, 0) + 1
            
            # Final anagram check
            for i in range(len(word1)):
                let = word1[i]
                if let not in word2Dict:
                    return False
                if word1Dict[let] != word2Dict[let]:
                    return False
            return True
        return isAnagram(s, t)
