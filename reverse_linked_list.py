"""
LeetCode #206: Reverse Linked List
Given the head of a singly linked list, reverse the list and return the new head.
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev


def reverse_list_recursive(head):
    """Recursive approach."""
    if not head or not head.next:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head


def to_list(head):
    """Convert linked list to Python list for easy printing."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def from_list(arr):
    """Convert Python list to linked list."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


if __name__ == "__main__":
    head = from_list([1, 2, 3, 4, 5])
    print(f"Original: {to_list(head)}")
    reversed_head = reverse_list(head)
    print(f"Reversed: {to_list(reversed_head)}")
