'''

33. Search in Rotated Sorted Array
Medium

7434

653

Add to List

Share
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-10^4 <= nums[i] <= 10^4
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-10^4 <= target <= 10^4
 

Follow up: Can you achieve this in O(log n) time complexity?

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1
        
        
        while l <= r:
            m = (l+r) // 2
            print(l,m,r)
            
            
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]:
                if nums[m] >= target >= nums[l]:
                    r = m-1
                    
                else:
                    l = m + 1
                    
            else:
                if nums[r] >= target >= nums[m]:
                    l = m+1
                else:
                    r = m-1
                    
        return -1

