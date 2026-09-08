class Solution:
    def isAnagram(self, s: str, t: str) -> bool:    
        # convert both to dict -> let:freq
        # go through dict to check if they are equal
        sDict = {}
        # {a:1, b:3}
        for i in range(len(s)):
            char = s[i]
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        for char in t:
            if char in sDict:
                sDict[char] -= 1
            else:
                return False # not anagram 
        # if anagram then sDict.values will just be an array of values
        for freq in sDict.values():
            if freq != 0:
                return False # not anagram

        return True


                
