class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char.lower() for char in s if char.isalnum())
        print(s)
        l = len(s)

        for i in range((l+1//2)):
            j = l-i-1
            print(f'{i} != {j}')
            print(f'{s[i]} != {s[j]}')
            if s[i] != s[j]:
                return False
        
        return True

        