class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            "v": self.value,
            "l": self.left.to_dict() if self.left else {},
            "r": self.right.to_dict() if self.right else {},
        }

def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    if not preorder and not inorder:
        return {}

    root_value = preorder[0]
    root_index = inorder.index(root_value)

    left_subtree = tree_from_traversals(preorder[1:root_index+1], inorder[:root_index])
    right_subtree = tree_from_traversals(preorder[root_index+1:], inorder[root_index+1:])

    if isinstance(left_subtree, Node):
        left_subtree = left_subtree.to_dict()
    if isinstance(right_subtree, Node):
        right_subtree = right_subtree.to_dict()

    return {
        "v": root_value,
        "l": left_subtree,
        "r": right_subtree,
    }