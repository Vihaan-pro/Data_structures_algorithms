class Tree_node():
    def __init__(self,data):
        self.data = data
        self.children = []  # this is the list of children

root = Tree_node("1")
nodeb = Tree_node("2")
nodec = Tree_node("3")
noded = Tree_node("4")
nodee = Tree_node("5")
nodef = Tree_node("6")
nodeg = Tree_node("7")

root.children.append(nodeb) # adding children to the root
root.children.append(nodec)
root.children.append(noded)

nodeb.children.append(nodee)
nodeb.children.append(nodef)

nodec.children.append(nodeg)



def  preorder_traversal(root):
    if root:
        print(root.data, end= " ")
        for i in root.children:
            preorder_traversal(i)

print ("preorder_traversal nd tree is ")

preorder_traversal(root)

