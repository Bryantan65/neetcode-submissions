class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_vals = set()

        for i in nums:
            unique_vals.add(i)
        
        if len(unique_vals) < len(nums):
            return True
        else:
            return False
          