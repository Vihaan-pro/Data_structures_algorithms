class Tree_node():# binary tree emaple
    def __init__(self,data):
        self.data = data  # the values stored in the node 
        self.left = None # ref. to left child (nodes)
        self.right = None
# root - left - right
root = Tree_node("CEO")
root.left = Tree_node("VP Engineering")
root.right = Tree_node("VP Sales")
root.left.left = Tree_node("Senior Engineer")
root.left.right = Tree_node("Junior Engineer")
root.right.left = Tree_node("Sales Manager")
root.right.right = Tree_node("Sales Rep")

def  preorder_traversal(root):
    if root is None:
        return
    print(root.data)
    preorder_traversal(root.left)
    preorder_traversal(root.right)
    

preorder_traversal(root)