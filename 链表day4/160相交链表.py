class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p,q = headA,headB
        while p != q:
            if p:
                p = p.next
            else:
                p = headB
            if q:
                q = q.next
            else:
                q = headA
        return p