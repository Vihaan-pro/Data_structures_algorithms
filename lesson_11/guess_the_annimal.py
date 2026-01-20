Tree = {"question":"does it fly",
        "yes":{"question": "is it a bird",
               "yes":"crow","no": "bat"}, 
               "no":{"question": "is it a pet",
                     "yes":"dog", "no" : "mamba"}
         
            }

def play(node):
    if type (node) == str:
        print("I guessed it is",node)
        return
    awnser = input(node["question"]+ " (yes/no) ")
    play(node[awnser])

play(Tree)

