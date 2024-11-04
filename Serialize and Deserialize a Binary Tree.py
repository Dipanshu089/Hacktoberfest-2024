# A program to serialize and deserialize a binary tree. 
# Serialization is the process of converting a tree into a string format, and
# Deserialization is the process of converting that string back into the original tree structure.


# Example usage:
# Tree structure:
#     1
#    / \
#   2   3
#      / \
#     4   5

"""
# Create tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

codec = Codec()
tree_string = codec.serialize(root)
print(tree_string)   # Output: A serialized string (like "1,2,#,#,3,4,#,#,5,#,#")
reconstructed_tree = codec.deserialize(tree_string)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                vals.append("#")
                return
            vals.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        vals = []
        dfs(root)
        return ",".join(vals)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        def dfs():
            val = next(vals)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(","))
        return dfs()
