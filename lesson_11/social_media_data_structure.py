class Tree_node():
    def __init__(self,name):
        self.name = name
        self.friends = []  # this is the list of children
    def add_friends(self,friend):
        self.friends.append(friend)
    def display(self,level = 0):
        print("  "* level*2+self.name)
        for i in self.friends:
            i.display(level+1)


root = Tree_node("Vihaan")
nodeb = Tree_node("Ravi")
nodec = Tree_node("Manoj")
noded = Tree_node("Rajesh")
nodee = Tree_node("Avi")

root.add_friends(nodeb)
root.add_friends(nodec)

nodeb.add_friends(noded)
nodec.add_friends(nodee)

root.display()