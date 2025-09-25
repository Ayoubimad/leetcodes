"""Merge two sorted linked lists and return it as a new sorted list.
The new list should be made by splicing together the nodes of the first two lists.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # creo un array per mettere i dati di entrambe le liste

        merged = []

        while list1 is not None:

            merged.append(list1.val)
            list1 = list1.next

        while list2 is not None:

            merged.append(list2.val)
            list2 = list2.next

        if not merged:
            return None

        # ordino bubble sort

        s = False

        while s is False:

            s = True

            for i in range(len(merged) - 1):

                if merged[i] > merged[i + 1]:

                    tmp = merged[i + 1]
                    merged[i + 1] = merged[i]
                    merged[i] = tmp

                    s = False

        print(merged)

        head = ListNode(val=merged[0])
        current = head

        for i in range(1, len(merged)):

            current.next = ListNode(val=merged[i])
            current = current.next

        return head
