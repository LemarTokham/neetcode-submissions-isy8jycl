class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        # {num: freq}
        # {1: 1, 2: 2, 3: 3}, k = 2
        # first max = 3, key is 3
        # second max = 2, key is 2

        # e.g 2:
        # {7: 2}, k = 1 
        # first max = 2, key is 7
        numFreq = defaultdict(int) # {num: 0}
        for i in range(len(nums)):
            numFreq[nums[i]] += 1


        arr = []
        for num, freq in numFreq.items():
            arr.append([freq, num]) # reverse so we can sort by freq later
        arr.sort() 

        # loop k times and extract the num
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])

        return res
    
        # for each val in dict, 

        # return largest k freqs
        # - find the max k times