class Solution(object):
    def removeNthFromEnd(self, head, n):

        # Reverse function
        def reverse(head):
            prev = None
            current = head

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt

            return prev

        # Step 1: Reverse the list
        head = reverse(head)

        # Step 2: Delete nth node from the beginning
        if n == 1:
            head = head.next
        else:
            current = head

            for _ in range(n - 2):
                current = current.next

            current.next = current.next.next

        # Step 3: Reverse again
        return reverse(head)