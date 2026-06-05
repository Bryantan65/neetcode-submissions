class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        hashmap2 = {}
        for i in s:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in t:
            if i in hashmap2:
                hashmap2[i] = hashmap2[i]+ 1
            else:
                hashmap2[i] = 1
 
        if hashmap == hashmap2:
            return True
        return False