class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seq_len = 1
        max_seq = 0
        for i in range(len(nums)):
            seq_len = 1
            curr_num = nums[i]
            # check for start of seq
            if curr_num - 1 not in num_set:
                while curr_num+1 in num_set:
                    seq_len += 1
                    curr_num +=1

            max_seq = max(seq_len,max_seq)
            print(max_seq, seq_len)
            
        return max_seq
            
