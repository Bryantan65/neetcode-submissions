class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #what is a permutation
        truth = {}
        current = {}
        l = 0

        for i in (s1):
            truth[i] = truth.get(i,0)+1
        
        

        for r in range(len(s2)):
            current[s2[r]] = current.get(s2[r],0)+1
            if (r-l+1) > len(s1):
                current[s2[l]] -=1
                if current[s2[l]] == 0:
                    del current[s2[l]]
                l+=1
            if current == truth:
                return True
        return False
        
            

        
        



        