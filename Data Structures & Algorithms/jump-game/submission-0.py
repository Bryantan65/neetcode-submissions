class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        curr_pos = 0
        furthest = 0

        for i in range(len(nums)):
            
            print("i=", i,"furthest=",furthest,"numsi=", nums[i],)
            if furthest < i:
                print("INVALID")
                return False
            furthest = max(furthest,i+nums[i])
            
            
        return True
            
            