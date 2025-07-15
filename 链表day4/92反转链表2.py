class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        p0 = dummy
        
        for i in range(left -1):
            p0 = p0.next
        pre = None
        cur = p0.next
        for i in range(right-left+1):
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        p0.next.next=cur
        p0.next = pre
        return dummy.next