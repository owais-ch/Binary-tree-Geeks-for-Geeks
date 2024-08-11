'''
Mirror Tree (GFG)
Given a Binary Tree, convert it into its mirror.
MirrorTree1            

Example 1:

Input:
      1
    /  \
   2    3
Output: 3 1 2
Explanation: The tree is
   1    (mirror)  1
 /  \    =>      /  \
2    3          3    2
The inorder of mirror is 3 1 2
'''

class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        def traversal(root):
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            if root.right:
                traversal(root.right)
                
            root.left,root.right=root.right,root.left
            
            return root
            
        return traversal(root)
