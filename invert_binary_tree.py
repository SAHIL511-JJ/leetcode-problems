"""
LeetCode #226: Invert Binary Tree
Invert a binary tree (mirror it).
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root


def invert_tree_iterative(root):
    """Iterative approach using a stack."""
    if not root:
        return None

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root


def level_order(root):
    """Helper to print tree in level order."""
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        level = []
        next_queue = []
        for node in queue:
            level.append(node.val)
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        result.append(level)
        queue = next_queue

    return result


if __name__ == "__main__":
    tree = TreeNode(
        4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
    )
    print(f"Original: {level_order(tree)}")
    invert_tree(tree)
    print(f"Inverted: {level_order(tree)}")
