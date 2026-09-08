class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1,cur1 = 0,0
        prev2,cur2 = 0,0
 

        for n in nums[:-1]:
            temp = max(n+prev1,cur1)
            prev1=cur1
            cur1 = temp

        # print(temp1)
      
        
        for n in nums[1:]:
            temp = max(n+prev2,cur2)
            prev2=cur2
            cur2 = temp
        
        if nums[0] > max(cur1,cur2):
            return nums[0]
        return max(cur1,cur2)
        