class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointer approach
        # Use a pointer k to track the position where the next valid element should go.
        # Loop through the array:

        # If the current element is not equal to val, copy it to nums[k] and increment k.


        # After the loop, the first k elements contain the result.
        
        k = 0  # Pointer for placing valid elements
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k


