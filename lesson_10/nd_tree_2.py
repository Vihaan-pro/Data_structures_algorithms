class Tree_node():
    def __init__(self,data):
        self.data = data
        self.children = []  # this is the list of children

root = Tree_node("a")
nodeb = Tree_node("b")
nodec = Tree_node("c")
noded = Tree_node("d")
nodee = Tree_node("e")

root.children.append(nodeb) # adding children to the root
root.children.append(nodec)
root.children.append(noded)
root.children.append(nodee)


def  postorder_traversal(root):
    if root:
        for i in root.children:
            postorder_traversal(i) # recursivly visiting the child
        print(root.data, end= " ") 

print ("postorder_traversal nd tree is ")

postorder_traversal(root)

