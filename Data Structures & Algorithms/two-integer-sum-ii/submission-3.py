class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = 1
        start = len(numbers)
      


        for i in range(start):
            

            for j in range(start):

                if j <= p1:
                    print("skipped" , j)
                else:
                    if(numbers[i] + numbers[j]== target):
                        return [i+1,j+1]
      
            p1 +=1
        return False 
            
                
            
            
   
                
                
  