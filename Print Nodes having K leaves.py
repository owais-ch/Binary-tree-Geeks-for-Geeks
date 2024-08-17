
'''
Print Nodes having K leaves (GFG)

Given a binary tree and an integer value K, the task is to find all nodes data in the given binary tree having exactly K leaves in sub-tree rooted with them.

NOTE: Nodes should be printed in the order in which they appear in postorder traversal.

Example 1:

Input:
K = 1
      0
    /   \
   1     2
Output: -1
Explanation: There is no node in this
tree which has one leaf in the sub tree
below it.
'''

class Solution:
    # Your task is to complete this function
    # function should print the node whose subtrees has exactly k leaves 
    # if no such leaves is present print -1    
    def btWithKleaves(self, root, k):
        def traversal(root):
            if root==None:
                return 0
                
            lsum=traversal(root.left)
            rsum=traversal(root.right)
            
            value=1 if root.left==None and root.right==None else 0
            
            if lsum+rsum==k:
                list1.append(root.data)
                
            total=lsum+rsum+value
            return total
           
        
        list1=[]
        
        traversal(root)
        
        if list1==[]:
            return [-1]
        return list1
