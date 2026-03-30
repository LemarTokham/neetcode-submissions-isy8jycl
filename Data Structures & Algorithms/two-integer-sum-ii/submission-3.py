class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        l = 0
        r = len(numbers) - 1
        for i in range(len(numbers)):
            numSum = numbers[l] + numbers[r]
            if numSum > target:
                r = r - 1
            elif numSum < target:
                l = l + 1
            else: # they are the same
                # Convert to 1-indexed
                return [l+1, r+1]

                
        
            