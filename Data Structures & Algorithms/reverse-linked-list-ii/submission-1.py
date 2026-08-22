# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(l):
            if not l:
                return None
            curr = l
            prev = None
            while curr:
                next_ = curr.next
                curr.next = prev
                prev = curr
                curr = next_

            return prev
        if left != right:
            if left == 1:
                place = 1
                curr = head
                while place < right:
                    place += 1
                    curr = curr.next
                    
                
                l1 = head
                l2 = curr.next
                curr.next = None
                l3 = reverseList(l1)
                newCurr = l3
                while newCurr.next:
                    newCurr = newCurr.next

                newCurr.next = l2
                
                return l3
            else:
                place = 1
                prev = None
                curr = head
                while place < left:
                    place += 1
                    prev = curr
                    curr = curr.next
                
                l1 = curr
                while place < right:
                    place += 1
                    curr = curr.next

                l3 = curr.next
                curr.next = None
                l2 = reverseList(l1)
                prev.next = l2
                l1.next = l3

                return head
        else:
            return head