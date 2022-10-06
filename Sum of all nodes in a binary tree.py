'''Give an algorithm for finding the sum of all elements in a binary tree.'''

def sum_all(root):
    global sum1
    
    if root==None:
        return 0
    
    sum1+=root.data
    
    if root.left:
        sum_all(root.left)
        
    if root.right:
        sum_all(root.right)
