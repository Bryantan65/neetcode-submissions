class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        mydict = {}
        maximum =0
        maxf = 0

        for r in range(len(s)):
            mydict[s[r]] = mydict.get(s[r],0) + 1
            maxf = max(mydict.values())
            while (r-l+1)-maxf > k:
                print("triggered", len(mydict))
                mydict[s[l]] -= 1
                if mydict[s[l]] == 0:
                    del mydict[s[l]]
                l+=1
            maximum = max(maximum, (r-l+1))
        return maximum


            
   