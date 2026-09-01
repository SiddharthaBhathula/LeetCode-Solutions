class Solution:
    def isPalindrome(self, X: int) -> bool:
        if X <  0: return False
        
        div = 1 
        while X >= 10 * div:
            div *= 10

        while X:
            if X // div != X %10 : return False
        
            X = (X % div) // 10 
            div = div / 100

        return True