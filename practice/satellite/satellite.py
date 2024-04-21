# Node class represents a node in the binary tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    # Convert the node and its children into a dictionary
    def to_dict(self):
        return {
            "v": self.value,
            "l": self.left.to_dict() if self.left else {},
            "r": self.right.to_dict() if self.right else {},
        }

# Function to construct a binary tree from its preorder and inorder traversals
def tree_from_traversals(preorder, inorder):
    # Check if the lengths of preorder and inorder are the same
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    # Check if the sorted lists are the same (which means they contain the same elements)
    if sorted(preorder) != sorted(inorder):
        raise ValueError("traversals must have the same elements")
    # Check if the elements in the lists are unique
    if len(set(preorder)) != len(preorder):
        raise ValueError("traversals must contain unique items")

    # If both preorder and inorder are empty, return an empty dictionary
    if not preorder and not inorder:
        return {}

    # Find the root of the tree from the preorder traversal
    root_value = preorder[0]
    root_index = inorder.index(root_value)

    # Split the preorder and inorder traversals into left and right subtrees
    left_subtree = tree_from_traversals(preorder[1:root_index+1], inorder[:root_index])
    right_subtree = tree_from_traversals(preorder[root_index+1:], inorder[root_index+1:])

    # Convert the left and right subtrees to dictionaries if they are Node instances
    if isinstance(left_subtree, Node):
        left_subtree = left_subtree.to_dict()
    if isinstance(right_subtree, Node):
        right_subtree = right_subtree.to_dict()

    # Return a dictionary representing the tree
    return {
        "v": root_value,
        "l": left_subtree,
        "r": right_subtree,
    }