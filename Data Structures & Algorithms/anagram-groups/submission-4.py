class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramList = []
        seenIndex = set() # set so fast lookup
        for i in range(len(strs)):
            print(i ,seenIndex)
            if i in seenIndex:
                continue
            currWord = strs[i]
            anagrams = [currWord] # [act]
            for j in range(i + 1, len(strs)):
                # if we are on last elem of list, j will be out of bounds
                if j >= len(strs): 
                    break

                compWord = strs[j]

                # check if anagram
                if self.checkAnagram(currWord,compWord):
                    anagrams.append(compWord)
                    # we have seen dealth with this word already so skip it next time
                    seenIndex.add(j)
                # if not anagram we skip op entierly
                
            anagramList.append(anagrams)

        return anagramList
        

    def checkAnagram(self, s, t):
        if len(s) != len(t):
            return False
        # Checks if two words are anagrams of each other
        s_dict, t_dict = {}, {}
        for i in range(len(s)):
            s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        for i in range(len(t)):
            t_dict[t[i]] = t_dict.get(t[i], 0) + 1

        return s_dict == t_dict # true if anagram
            