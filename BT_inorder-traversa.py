# Definition for a binary tree node.inorder traversal

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #inorderTraversal=left->root->right
        ans=[]
        def inorder(node):
            if not node:
                return 
            inorder(node.left)     
            ans.append(node.val)   # ans  se  store root node ki val append krne k liye
            inorder(node.right)    
        inorder(root)
        return ans
