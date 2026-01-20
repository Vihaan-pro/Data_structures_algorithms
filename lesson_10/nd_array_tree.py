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


def  preorder_traversal(root):
    if root:
        print(root.data, end= " ")
        for i in root.children:
            preorder_traversal(i)

print ("preorder_traversal nd tree is ")

preorder_traversal(root)

