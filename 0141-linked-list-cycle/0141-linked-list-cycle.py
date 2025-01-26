# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: #handels the edge cases
            return False

        slow = head
        fast = head.next

        while fast and fast.next:  # Ensure fast and fast.next are valid
            if fast == slow:  # Cycle detected
                return True
            slow = slow.next  # Move slow pointer by one step
            fast = fast.next.next  # Move fast pointer by two steps

        return False  # No cycle detected