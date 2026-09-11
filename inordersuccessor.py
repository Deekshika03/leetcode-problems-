"""
class Solution:
    def inorderSuccessor(self, root, p):
        successor = None

        while root:
            if p.val < root.val:
                successor = root
                root = root.left

            else:
                root = root.right

        return successor

        """

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def inorder_successor(root, x):
    successor = None

    while root:
        if x < root.key:
            successor = root
            root = root.left

        elif x > root.key:
            root = root.right

        else:
            # Case 1: Right subtree exists
            if root.right:
                root = root.right

                while root.left:
                    root = root.left

                successor = root

            break

    return successor


# BST create karna
root = Node(50)
root.left = Node(30)
root.right = Node(70)
root.left.left = Node(20)
root.left.right = Node(40)
root.right.left = Node(60)
root.right.right = Node(80)

# Successor find karo
x = 40
result = inorder_successor(root, x)

if result:
    print("Inorder Successor:", result.key)
else:
    print("No Inorder Successor")
