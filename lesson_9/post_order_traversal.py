class Tree_node():# binary tree emaple
    def __init__(self,data):
        self.data = data  # the values stored in the node 
        self.left = None # ref. to left child (nodes)
        self.right = None
#  left - right - root
root = Tree_node(1)
root.left = Tree_node(2)
root.right = Tree_node(3)
root.left.left = Tree_node(4)
root.left.right = Tree_node(5)
root.right.left = Tree_node(6)
root.right.right = Tree_node(7)

def  postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)
    

postorder_traversal(root)





        