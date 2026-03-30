class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0,0
        maxRes = 0
        charDict = {}
        maxf = 0
        while r < len(s): 
            charDict[s[r]] = 1 + charDict.get(s[r], 0) # either add to what we have or init with 1
            
            # find the most commonly occuring let
            maxf = max(maxf, charDict[s[r]])

            # do length - most commonly occuring: shows us the number of replications we do
            if (r - l) + 1 - maxf <= k:
                maxRes = max((r - l) + 1, maxRes)
            else: # move left side of window to be past invalid stage
                charDict[s[l]] -= 1
                charDict[s[r]] -= 1 # gets put back in when the loop starts, so stops it from being incremented twice
                l += 1
                continue
            r+= 1
        
        return maxRes