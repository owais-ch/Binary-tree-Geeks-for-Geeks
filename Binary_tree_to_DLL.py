'''
Binary Tree To DLL (GFG)

Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. The order of nodes in DLL must be the same as the order of the given Binary Tree. The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.

TreeToList

Examples:

Input:
      1
    /  \
   3    2
Output:
3 1 2 
2 1 3

Explanation: DLL would be 3<=>1<=>2
'''

class Solution:
    def bToDLL(self,root):
        def traversal(root):
            nonlocal count,head,n
            if root==None:
                return None
                
            if root.left:
                traversal(root.left)
                
            if count==0:
                head=root
                n=head
                count+=1
            else:
                n.right=root
                root.left=n
                n=n.right
            
            if root.right:
                traversal(root.right)
                
        count=0
        head=None
        n=None
        traversal(root)
        
        return head
