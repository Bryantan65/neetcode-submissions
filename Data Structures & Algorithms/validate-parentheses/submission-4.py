class Solution:
    def isValid(self, s: str) -> bool:
        

        masterdict = {")": "(", "]":"[", "}":"{"}
        stack = []

       

        for i in s:
            print(i)
            if stack and i in masterdict and stack[-1] == masterdict[i]: #if a closing bracket exists (key), 
                stack.pop()
        
            else: #opening bracket
                stack.append(i)
            
        print(stack)
        return not stack

        