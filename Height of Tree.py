'''
Height of Tree (GFG)
Given a binary tree, find its height.

Example 1:

Input:
     1
    /  \
   2    3
Output: 2
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        if root==None:
            return 0
                
        lh=self.height(root.left)
        rh=self.height(root.right)
            
        return max(lh,rh)+1
