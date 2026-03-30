class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        control = strs[0]
        for word in strs[1:]:
            i = 0
            while i < len(word) and i < len(control) and control[i] == word[i]:
                i+=1
            control = control[:i]                 
        return control
