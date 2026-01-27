class Graph():
    def __init__(self):
        self.friends = {}
    def add_edge(self,person1,person2):
        if person1 not in self.friends:
            self.friends[person1]= [] # if the person1 not in dictionary + in dictionary as the key
        if person2 not in self.friends:
            self.friends[person2]= []
        self.friends[person1].append(person2)
        self.friends[person2].append(person1) # both are keys so both are values to each other
        
    def show_graph(self):
        for i,j in self.friends.items():
            print(i , "is friends with",j)
friendship_graph = Graph()
friendship_graph.add_edge("a","b")
friendship_graph.add_edge("a","c")
friendship_graph.add_edge("b","d")

friendship_graph.show_graph()

