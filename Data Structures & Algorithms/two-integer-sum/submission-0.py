class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3,4,5,6] = 7
        # 2 for loops
        # for each number, [3], look through every OTHER number , 4 5 6
        ans = []
        for i,num in enumerate(nums):
            for i2, num2 in enumerate(nums[i+1:],start = i+1):
                if num + num2 == target:
                    # print("HIT")
                    ans.append(i)
                    ans.append(i2)
                    return ans
            # print(i, num)
        
        return False