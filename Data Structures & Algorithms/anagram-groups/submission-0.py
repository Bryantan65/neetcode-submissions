class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #sub list from list

        #input ['rat','tar']
        #output [[rat,tar] [wtv else matches]]

        #loop through every string in the list, "act"
        #loop through each char in a string a:1 c:1 t:1 -> dict1?
        # act = {act, cat etc}
        
        hashmap = {}
        result = []

        for i in strs:
            hashmap[tuple(sorted(i))] = hashmap.get(tuple(sorted(i)), []) + [i] 
        
        for key,val in hashmap.items():
            result.append(val)
        
        return result
        
            


        