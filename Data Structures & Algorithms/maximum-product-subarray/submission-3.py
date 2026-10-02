class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMax = curMin = largest = nums[0]

        if len(nums)==1:
            return nums[0]
        l=0
        for r in range(1,len(nums)):
            
            x = nums[r]
            candidates = (x, curMax*x, curMin*x)
            curMax, curMin = max(candidates), min(candidates)
            largest = max(largest, curMax)
            l+=1
        return largest