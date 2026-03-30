class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(index, target, nums):
            
            if not len(nums):
                return []
            l = 0
            r = len(nums) -1
            res = []
            while l < r:

                numSum = nums[l] + nums[r]
                if numSum > target:
                    r = r-1
                elif numSum < target:
                    l=l+1
                else:
                    res.append([nums[l], nums[r]])
                    print(r)
                    l+=1
                    r-=1
            return res

        nums.sort()
        final_res = set()
        seen = set()
        for i in range(len(nums)):
            # if nums[i] in seen:
            #     continue
            # else:
            #     seen.add(nums[i])
            # print(f'seen: {seen}')
            currNum = nums[i]
            print("currnum:", currNum)
            twoSum_op = twoSum(i, -currNum, nums[i+1:])
            if twoSum_op:
                for arr in twoSum_op:
                    arr.append(currNum)
                    arr.sort()
                    final_res.add(tuple(arr))
                
        print(final_res)
        return [list(t) for t in final_res]
            







            