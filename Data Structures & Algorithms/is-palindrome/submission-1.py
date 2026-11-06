class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        l = len(s)

        for i in range((l+1//2)):
            j = l-i-1
            if s[i] != s[j]:
                return False
        
        return True

        