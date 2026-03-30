class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        maxRes = 0
        charDict = {}
        while r < len(s):
            # Every iteration is counting the lenght of the list
            if s[r] in charDict:
                charDict[s[r]] += 1
            else:
                charDict[s[r]] = 1
            
            # find the most commonly occuring let
            maxLet = ""
            maxFreq = 0
            for let, freq in charDict.items():
                if freq > maxFreq:
                    maxFreq = freq
                    maxLet = let

            # do length - most commonly occuring: shows us the number of replications we do
            if (r - l) + 1 - maxFreq <= k:
                maxRes = max((r - l) + 1, maxRes)
            else: # move left side of window to be past invalid stage
                charDict[s[l]] -= 1
                charDict[s[r]] -= 1
                l += 1
                continue
            r+= 1
        
        return maxRes