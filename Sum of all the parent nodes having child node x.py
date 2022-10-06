'''Given a binary tree containing n nodes. The problem is to find the sum of all the parent node’s which have a child node with value x.'''

def sum_child(root,x):
    global sum1
    if root==None:
        return None
    
    if root.left:
        if root.left.data==x:
            sum1+=root.data
        elif root.right:
            if root.right.data==x:
                sum1+=root.data
    elif root.right:
        if root.right.data==x:
            sum1+=root.data
            
    if root.left:
        sum_child(root.left,x)
        
    if root.right:
        sum_child(root.right,x)
