class Tree_node():# binary tree emaple
    def __init__(self,data):
        self.data = data  # the values stored in the node 
        self.left = None # ref. to left child (nodes)
        self.right = None
#  left - right - root
root = Tree_node("Principal")
root.left = Tree_node("Academic Dean")
root.right = Tree_node("Administrative Dean")
root.left.left = Tree_node("Math Teacher")
root.left.right = Tree_node("Science Teacher")
root.right.left = Tree_node("Librarian")
root.right.right = Tree_node("Counselor")

def  postorder_traversal(root):
    if root is None:
        return
    postorder_traversal(root.left)
    postorder_traversal(root.right)
    print(root.data)
    

postorder_traversal(root)