class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            while (r-l +1) - max(count.values()) > k: #while INVALID
                count[s[l]] -=1 #reduce the count 
                l+=1 #move L
            res = max(res, (r-l+1))
        return res


        