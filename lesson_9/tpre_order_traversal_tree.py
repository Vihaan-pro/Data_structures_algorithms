class Tree_node():# binary tree emaple
    def __init__(self,data):
        self.data = data  # the values stored in the node 
        self.left = None # ref. to left child (nodes)
        self.right = None
# root - left - right
root = Tree_node(1)
root.left = Tree_node(2)
root.right = Tree_node(3)
root.left.left = Tree_node(4)
root.left.right = Tree_node(5)
root.right.left = Tree_node(6)
root.right.right = Tree_node(7)

def  preorder_traversal(root):
    if root is None:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    

preorder_traversal(root)





        