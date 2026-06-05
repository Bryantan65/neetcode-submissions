class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#hello
        
        encoded = ""
        for i in strs:
            encoded = encoded +  str(len(i)) + "#" + i
        return encoded    

    def decode(self, s: str) -> List[str]:
        #given 5#hello5#world make it [Hello,World]
        res = []
        i=0
        while i< len(s):
            j=i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            res.append(s[j+1: j+1+length])
            i = j + 1 + length
        return res