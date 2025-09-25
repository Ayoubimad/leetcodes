"""217. Contains Duplicate - Easy
Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

"""

# Con approccio brute force

"""
class Solution(object):
    def containsDuplicate(self, nums):

        :type nums: List[int]
        :rtype: bool

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        hash_table = (
            {}
        )  # metto gli elementi in una hash_table {element : occurrence}, appena occurrence è > 1 ritorno True

        for element in nums:
            # If a collision occurs, it means we have already inserted an element in the hash_table
            if element in hash_table:
                return True
            else:
                hash_table[element] = 1

        return False
