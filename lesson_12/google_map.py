class Graph():
    def __init__(self):
        self.friends = {}
    def add_edge(self,city1,city2,city3,city4):
        if city1 not in self.friends:
            self.friends[city1]= [] # if the person1 not in dictionary + in dictionary as the key
        if city2 not in self.friends:
            self.friends[city2]= []
        if city3 not in self.friends:
            self.friends[city3]= []
        if city4 not in self.friends:
            self.friends[city4]= []
        self.friends[city1].append(city2)
        self.friends[city2].append(city1) # both are keys so both are values to each other
        self.friends[city3].append(city4)
        self.friends[city4].append(city3)
        
    def show_graph(self):
        for i,j in self.friends.items():
            print(i , "is friends with",j)
friendship_graph = Graph()
friendship_graph.add_edge("city4","city3","city1","city2")
#friendship_graph.add_edge("city1","city3")
#friendship_graph.add_edge("city3","city4")

friendship_graph.show_graph()

