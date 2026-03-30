class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False # must be same lenght to be valid

        # Create map for both strings
        sDict = {}
        tDict = {}
        for i in range(len(s)):
            current_let_in_s = s[i]
            current_let_in_t = t[i]
            # Making sure the letter exisits in the other string otherwise no point continuing
            if current_let_in_s not in t:
                return False
            if current_let_in_s in sDict:
                sDict[current_let_in_s] += 1
            else:
                sDict[current_let_in_s] = 1
            if current_let_in_t in tDict:
                tDict[current_let_in_t] += 1
            else:
                tDict[current_let_in_t] = 1

        # Compare both maps to see if they have the same occurences
        # Reaching this point we have agreed that:
        # 1. Both strings are the same lenght
        # 2. Both strings have the same letters within them
        for let in s:
            if sDict[let] != tDict[let]:
                return False
        return True
