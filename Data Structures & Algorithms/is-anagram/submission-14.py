class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        for i in s:
            hashmap1[i] = hashmap1.get(i, 0) + 1

        for j in t:
            hashmap2[j] = hashmap2.get(j, 0) + 1
        
        return hashmap1 == hashmap2
        

        

            

            
        
        
        