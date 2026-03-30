class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start from 0 -> 2
        # start from 1 -> 7
        numDict = {}
        for i in range(len(nums)):
            numDict[nums[i]] = 1
        
        max_seq = 0
        for i in range(len(nums)):
            count = 1
            curr_num = nums[i]
            while curr_num + 1 in numDict:
                count += 1
                curr_num += 1
            if count > max_seq:
                 max_seq = count
        return max_seq

            