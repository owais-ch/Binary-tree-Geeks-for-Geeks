'''
Balanced Tree Check (GFG)

Given a binary tree, find if it is height balanced or not.  A tree is height balanced if difference between heights of left and right subtrees is not more than
one for all nodes of tree. 

Examples:

Input:
      1
    /
   2
    \
     3 
Output: 0
Explanation: The max difference in height of left subtree and right subtree is 2, which is greater than 1. Hence unbalanced
'''

class Solution:
    def isBalanced(self,root):
        def height(root):
            nonlocal value
            if root==None:
                return 0
                
            lh=height(root.left)+1
            rh=height(root.right)+1
            
            if abs(lh-rh)>1:
                value=0
                
            hh=max(lh,rh)
            
            return hh
            
                
            
        value=1        
        height(root)
        
        return value
