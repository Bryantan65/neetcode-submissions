class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # loop through the array
        # start from smallest num
        # always check for next consecutive number (maybe value + 1), keep going until u cant go anymore

        copy = set(nums)

        if len(nums) == 0:
            return 0


        longest  = 0
       

        for num in copy:
            if num -1 not in copy:
                length  =1
                current = num
            
                while current + 1 in copy:
                    current+=1 
                    length +=1

                longest = max(longest, length)

        return longest 

        

        
        
    

     