class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for word in strs:
            s += str(len(word)) + "#" + word
        print(s)
        return s
    def decode(self, s: str) -> List[str]:
        countStrs = ''
        count = 0
        res = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                count = int(countStrs)
                print(count)
                res.append(s[i+1:i+1+count])
                i = i + count
                countStrs = ''
            else: # 'i' must be a number
                countStrs += s[i]
            i+=1
        return res