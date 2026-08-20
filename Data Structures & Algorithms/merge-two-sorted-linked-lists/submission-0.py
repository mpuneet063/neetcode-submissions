# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = node = ListNode()
        l1 = list1
        l2 = list2
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
                
            else:
                node.next = l2
                l2 = l2.next

            node = node.next
        node.next = l1 or l2
        return dummy.next