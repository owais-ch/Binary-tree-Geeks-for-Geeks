'''
Leaves at same level or Not (GFG) 
Given a binary tree with n nodes, determine whether all the leaf nodes are at the same level or not. Return true if all leaf nodes are at the same level, and false otherwise.

Example 1:

Input:
Tree:
    1
   / \
  2   3
Output:
true
Explanation:
The binary tree has a height of 2 and the leaves are at the same level.
'''

class Solution:
    #Your task is to complete this function
    #function should return True/False or 1/0
    def check(self, root):
        def traversal(root,height):
            nonlocal value,result
            if root==None:
                return None
                
            if root.left==None and root.right==None:
                if value==-1:
                    value=height
                else:
                    if value!=-1 and value!=height:
                        result=False
                        
            if root.left:
                traversal(root.left,height+1)
                
            if root.right:
                traversal(root.right,height+1)
                
        value=-1
        result=True
        
        traversal(root,0)
        
        return result
