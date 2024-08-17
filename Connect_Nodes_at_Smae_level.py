'''
Connect Nodes at Same Level (GFG)
Given a binary tree, connect the nodes that are at the same level. The structure of the tree Node contains an addition nextRight pointer for this purpose.

Initially, all the nextRight pointers point to garbage values. Your function should set these pointers to point next right for each node.

       10                       10 ------> NULL
      / \                       /      \
     3   5       =>     3 ------> 5 --------> NULL
    / \     \               /  \           \
   4   1   2          4 --> 1 -----> 2 -------> NULL

 

Example 1:

Input:
     3
   /  \
  1    2
Output:
3 1 2
1 3 2
Explanation:The connected tree is
       3 ------> NULL
     /   \
    1---> 2 -----> NULL
'''

class Solution:
    def connect(self, root):
        def traversal(root,h):
            if root==None:
                return None
                
            if h not in dict1:
                dict1[h]=[root]
            else:
                dict1[h].append(root)
            
            if root.left:
                traversal(root.left,h+1)
            
            if root.right:
                traversal(root.right,h+1)
                
        dict1=dict()
        
        traversal(root,0)
        
        for i in dict1:
            length=len(dict1[i])
            for j in range(1,length):
                dict1[i][j-1].nextRight=dict1[i][j]
        return root
