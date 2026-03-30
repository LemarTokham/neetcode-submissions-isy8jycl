class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        control = strs[0]
        count = 300
        for word in strs[1:]:
            print(word)
            curr = 0
            for i in range(len(word)):
                if i < len(control) and word[i] == control[i]:
                    print(i)
                    print("hi")
                    curr += 1
                else:
                    break
            count = min(curr, count)
        print(count)
        return control[:count]
