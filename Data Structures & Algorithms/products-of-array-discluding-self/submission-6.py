class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)

        for i in range(1, len(nums)):
            prev = nums[i-1]
            recent = pre[i-1]
            pre[i] = prev * recent
        print(pre)

        for i in range(len(nums) -2, -1, -1): # start at last index, end just before -1, go back -1 steps
            res = nums[i+1]
            recent = post[i+1]
            post[i] = res * recent
        print(post)

        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])

        return res