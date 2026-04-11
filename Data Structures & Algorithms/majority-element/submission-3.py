from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq= Counter(nums)
        ele= freq.most_common(1)[0][0]
        
        return ele

        