# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        """
        Adds two numbers represented by linked lists.

        The digits are stored in reverse order, so we can add
        corresponding nodes directly from left to right.

        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        """

        # Dummy node helps simplify linked-list construction.
        dummy = ListNode(0)
        current = dummy

        # Stores the carry from the previous addition.
        carry = 0

        # Continue until both lists and the carry are processed.
        while l1 or l2 or carry:

            # Get the current digit from each list.
            # Use 0 when one list has already ended.
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0

            # Add both digits along with the previous carry.
            total = digit1 + digit2 + carry

            # The current digit is the remainder after division by 10.
            digit = total % 10

            # The quotient becomes the carry for the next position.
            carry = total // 10

            # Create a new node containing the calculated digit.
            current.next = ListNode(digit)
            current = current.next

            # Move to the next node in each linked list.
            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        # Return the actual result, skipping the dummy node.
        return dummy.next
        