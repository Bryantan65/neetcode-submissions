class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = 99999999
        l,r = 0, len(nums)-1

        # [3,4,5,6,1,2]
        # [1,2,3,4,5,6]
        # mid = 5

        # how to find the smallest ? 

        # if right side bigger, r = mid-1

        # if left side smaller, l = mid+1
        # print(nums[0])
        while l<=r:
            mid = (l+r) // 2
            print("mid", nums[mid])
            if nums[r] > nums[mid]:
                r = mid-1
            else:
                l = mid+1
           
            minimum = nums[mid] if nums[mid] < minimum else minimum
            print(minimum)
        return minimum






        