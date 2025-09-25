"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2

Output: [1,2]

Example 2:

Input: nums = [1], k = 1

Output: [1]

Example 3:

Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

Output: [1,2]

"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}  # number: occurrence

        for num in nums:
            if num not in bucket:
                bucket[num] = 1
            else:
                bucket[num] = bucket[num] + 1

        # ordiniamo per valore, da quello che appare più frequentemente a quello meno frequente.
        sorted_bucket = dict(sorted(bucket.items(), key=lambda item: item[1]))
        # trasformo in lista di chiavi
        out = list(sorted_bucket.keys())
        # prendo gli ultimi k
        out = out[-k:]

        return out
