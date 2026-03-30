class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # start from 0 -> 2
        # start from 1 -> 7
        numDict = set(nums)
        
        max_seq = 0
     
        for i in range(len(nums)):
            count = 0
            curr_num = nums[i]
            if (curr_num - 1) not in numDict: # We have reached the start of a sequence
                count = 1
            while curr_num + 1 in numDict and count:
                count += 1
                curr_num += 1
            if count > max_seq:
                 max_seq = count

        return max_seq

            