class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sort by frequencies using lexico sorting or arrays
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        # convert to array and sort
        arr = []
        for num, freq in freq.items():
            arr.append([freq, num])
        arr.sort() # [count, num]

        # take k top nums
        res = []
        for i in range(k):
            res.append(arr.pop()[1]) # only keeps the actual num

        return res

