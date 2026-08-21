# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # cut in half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        l1 = head
        l2 = head2
        # reverse the second half
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return head
            curr = head
            prev = None
            while curr:
                next_ = curr.next           
                curr.next = prev
                prev = curr
                curr = next_
            return prev
        l2 = reverseList(l2)
        
        while l2:
            tmp1, tmp2 = l1.next , l2.next
            l1.next = l2
            l2.next = tmp1
            l1, l2 = tmp1, tmp2

            