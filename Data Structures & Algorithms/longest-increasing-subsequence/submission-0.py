class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l,r = 0,0
        longest = 0
        wtv = [1] * len(nums)

        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    wtv[i] = max(wtv[i],wtv[j]+1)
        return max(wtv)