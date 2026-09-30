class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        
        # l = 0
        for i in range(len(s)):

            l=r=i
            while l>=0 and r<len(s) and s[l] == s[r]:
                # print(l,r)
                l-=1
                r+=1
                res+=1
            
            l=i
            r=l+1
            while l>=0 and r<len(s) and s[l] == s[r]:
                # print("2nd for loop",l,r)
                l-=1
                r+=1
                res+=1
            

       
                
        
        return res




        
        