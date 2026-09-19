class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum =0
        max_sum = float('-inf')

        # for i in nums:
        #     if i < 0:
        #         max_sum = max(max_sum,i)
        #     elif i>0:
        #         cur_sum = i
        #         max_sum = max(max_sum, i)

        for i in range(len(nums)):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum<0:
                curr_sum = 0
        return max_sum

