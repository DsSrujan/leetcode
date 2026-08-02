# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if not head or not head.next or k == 0:
            return head

        # Find length
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1

        k = k % length
        if k == 0:
            return head

        # Rotate one step, k times
        for _ in range(k):
            current = head

            # Move to second-last node
            while current.next.next:
                current = current.next

            new_head = current.next      # Last node
            new_head.next = head         # Point last to old head
            current.next = None          # Break link
            head = new_head              # Update head

        return head