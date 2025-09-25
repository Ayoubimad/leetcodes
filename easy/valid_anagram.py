"""
242. Valid Anagram - Easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Metto ogni carattere di t e s in hash_tables differenti {"carattere": occorrenza}. Se sono uguali allora è un   anagramma.

        s_hash_table = {}
        t_hash_table = {}

        for element in s:
            if element in s_hash_table:
                s_hash_table[element] = s_hash_table[element] + 1
            else:
                s_hash_table[element] = 1

        for element in t:
            if element in t_hash_table:
                t_hash_table[element] = t_hash_table[element] + 1
            else:
                t_hash_table[element] = 1

        return s_hash_table == t_hash_table
