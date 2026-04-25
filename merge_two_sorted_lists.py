# Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
#
# Example 1:
#   Input: list1 = [1,2,4], list2 = [1,3,4]
#   Output: [1,1,2,3,4,4]
#
# Example 2:
#   Input: list1 = [], list2 = []
#   Output: []
#
# Example 3:
#   Input: list1 = [], list2 = [0]
#   Output: [0]
#
# Constraints:
#   The number of nodes in both lists is in the range [0, 50].
#   -100 <= Node.val <= 100
#   Both list1 and list2 are sorted in non-decreasing order.
#
# Approach:
#   Use a dummy node to start, and a pointer to build the new list.
#   Compare the current nodes of both lists, attach the smaller one to the result, and move that list's pointer forward.
#   Continue until one list is exhausted, then attach the remaining part of the other list.
#
#   Time Complexity: O(n + m) where n and m are the lengths of the two lists
#   Space Complexity: O(1) (excluding the output list)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    '''
    :type list1: ListNode
    :type list2: ListNode
    :rtype: ListNode
    '''
    dummy = ListNode()
    current = dummy
    
    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining elements
    current.next = list1 if list1 else list2
    
    return dummy.next

# Helper functions for testing
def list_to_linked_list(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Example usage:
if __name__ == '__main__':
    # Example 1
    list1 = list_to_linked_list([1, 2, 4])
    list2 = list_to_linked_list([1, 3, 4])
    merged = merge_two_lists(list1, list2)
    print('Example 1:')
    print('  Input: list1 = [1,2,4], list2 = [1,3,4]')
    print('  Output:', linked_list_to_list(merged))  # Expected: [1,1,2,3,4,4]
    print()
    
    # Example 2
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([])
    merged = merge_two_lists(list1, list2)
    print('Example 2:')
    print('  Input: list1 = [], list2 = []')
    print('  Output:', linked_list_to_list(merged))  # Expected: []
    print()
    
    # Example 3
    list1 = list_to_linked_list([])
    list2 = list_to_linked_list([0])
    merged = merge_two_lists(list1, list2)
    print('Example 3:')
    print('  Input: list1 = [], list2 = [0]')
    print('  Output:', linked_list_to_list(merged))  # Expected: [0]
    print()

