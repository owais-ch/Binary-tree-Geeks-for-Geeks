'''Consider lines of slope -1 passing between nodes (dotted lines in below diagram). 
The diagonal sum in a binary tree is the sum of all node’s data lying between these lines. Given a Binary Tree, print all diagonal sums.'''

def diagonal_sum(root):
    if root==None:
        return None
    
    hd=0
    
    q=[[root,hd]]
    
    dict1=dict()
    
    while q!=[]:
        node=q.pop()
        
        if node[-1] not in dict1:
            dict1[node[-1]]=node[0].data
        else:
            dict1[node[-1]]+=node[0].data
            
        hd=node[-1]
        
        if node[0].left:
            q.append([node[0].left,hd-1])
        if node[0].right:
            q.append([node[0].right,hd])
            
    return list(dict1.values())
