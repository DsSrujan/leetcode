class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Dummy node handles deleting the head easily
        dummy = ListNode(0)
        dummy.next = head

        slow = dummy
        fast = dummy

        # Move fast n + 1 steps ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers together
        while fast:
            slow = slow.next
            fast = fast.next

        # slow is now just before the node to delete
        slow.next = slow.next.next

        return dummy.next