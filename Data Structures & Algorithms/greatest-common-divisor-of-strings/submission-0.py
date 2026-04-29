from math import gcd
class Solution:

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        #If concatenations don't match, no common divisor string exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # GCD of lengths gives the largest possible divisor string length
        gcd_len = gcd(len(str1), len(str2))
        
        return str1[:gcd_len]
