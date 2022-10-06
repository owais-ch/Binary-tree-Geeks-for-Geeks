'''Given a Binary Tree, find the sum of all left leaves in it. '''

def sum_left(root):
    global sum1
    
    if root==None:
        return 0
    
    if root.left and root.left.left==None and root.left.right==None:
        sum1+=root.left.data
        
    if root.left:
        sum_left(root.left)
    if root.right:
        sum_left(root.right)
