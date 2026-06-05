class Solution:
    def isPalindrome(self, s: str) -> bool:
        boi = ""
        for i in s.lower():
            if i.isalnum():
                boi+=i
            print(boi)
        
        if boi != boi[::-1]:
            return False
        return True
            
        
        