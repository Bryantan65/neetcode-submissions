class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #enumerate the list so 0:-1 1:0 etc
        # mult all items except where index = i
        #FKKKKKKKKK time too long, so i failed
        # mult = 1
        # ans = []
        # for i in range(len(nums)):
        #     print("i =", i)
        #     for index, num in enumerate(nums):
        #         if(i != index):
        #             print("index =", index)
        #             mult= mult*num
                   
        #     ans.append(mult)
        #     #reset mult back to 1 if not number forever grows
        #     mult = 1

        # return ans

        n = len(nums)
        res = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            res[i] = prod
        return res
      
        


        
                
            
        
        