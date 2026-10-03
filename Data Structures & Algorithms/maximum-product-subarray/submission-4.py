class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        cur_max = 1
        cur_min =1
        total = nums[0]

        for i in nums:
            tmp = cur_max * i
            cur_max = max(i,cur_max*i,cur_min*i)
           
            cur_min = min(i,tmp,cur_min*i)
        
            total = max(cur_max,total)
        return total
        