import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = re.sub(r'[^a-zA-Z0-9]', '', s).lower()

        if temp == temp[::-1]:
            return True
        else: return False 

        