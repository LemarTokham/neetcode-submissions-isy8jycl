class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Checking for anagram between 2 words
        def isAnagram(word1, word2): # Total time complexity: O(n)
            if len(word1) != len(word2): # O(n)
                return False
            # Creating hashmaps for each word
            word1Dict = {}
            word2Dict = {}
            for i in range(len(word1)): # O(n)
                let = word1[i]
                word1Dict[let] = word1Dict.get(let, 0) + 1 # if key doesnt exist, init as 0, else increment
            for j in range(len(word2)): # O(n)
                let = word2[j]
                word2Dict[let] = word2Dict.get(let, 0) + 1
            
            # Final anagram check
            for i in range(len(word1)): # O(n)
                let = word1[i]
                if let not in word2Dict: # O(1) # Check if letter occurs in second word
                    return False
                if word1Dict[let] != word2Dict[let]: # O(1) # Check for same letter occurence
                    return False
            return True


        wordDict = {}
        flag = False
        for i in range(len(strs)):
            word = strs[i]
            # First check if it's an anagram with any word in dict
            for key in wordDict:
                if isAnagram(key, word):
                    wordDict[key].append(word)
                    flag = True
                    break # can only be anagram with one key
                
            if not flag:
                wordDict[word] = []
                
            flag = False
            
            

        # Convert to list
        result = []
        for key, values in wordDict.items():
            values.append(key)
            result.append(values)

        return result



                
            
            



                
    
                
            