class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        matching_i = {}
        Yeet = True
        for i in s:
            matching_i[i] = matching_i.get(i,0) + 1 
        #print(matching_i)
        if len(t) == len(s):
            for j in t:
                if j not in matching_i or t.count(j) != matching_i[j]:
                    print("yeet false triggered")
                    return False
                else:
                    yeet = True
           
            return yeet
        else:
            return False
                
        

            

            
        
        
        