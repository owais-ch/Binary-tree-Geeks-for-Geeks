'''
Root to leaf path sum (GFG)
Given a binary tree and an integer target, check whether there is a root-to-leaf path with its sum as target.

Examples :

Input: tree = 1, target = 2
            /   \
          2     3
Output: false
Explanation: There is no root to leaf path with sum 2.
'''

class Solution:
    def hasPathSum(self, root, target):
        def traversal(root):
            nonlocal value,sum1
            if root==None:
                return None
                
            sum1+=root.data
            
            if root.left==None and root.right==None:
                if sum1==target:
                    value=True
                    
            if traversal(root.left) or traversal(root.right):
                return True
                
            sum1-=root.data
            
            return False
            
        value=False
        sum1=0
        traversal(root)
        
        return value
