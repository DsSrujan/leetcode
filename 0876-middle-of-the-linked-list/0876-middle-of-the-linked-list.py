
class Solution(object):
    def middleNode(self, head1):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        fast=head1
        slow=head1
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow