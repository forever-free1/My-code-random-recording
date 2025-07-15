class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        right = dummy
        left = dummy
        for i in range(n):
            right = right.next
        
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return dummy.next