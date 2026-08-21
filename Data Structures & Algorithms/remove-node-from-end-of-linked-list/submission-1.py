# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length
        curr = head
        l = 0
        while curr:
            curr = curr.next
            l += 1
        N = l-n
        if not head.next:
            return None
        curr = head
        prev = None
        for _ in range(N):
            # while curr:
            prev = curr
            curr = curr.next

        print(curr.val)
        if prev:
            prev.next = curr.next
        else:
            head = curr.next
        return head