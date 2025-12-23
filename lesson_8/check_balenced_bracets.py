open_bracets = ["(","{","[","<"]
closing_brackets = [")","}","]",">"]

def check_brackets(my_str):
    stack = []
    for i in my_str:
        if i in open_bracets:
            stack.append(i)
        elif i in closing_brackets:
            pos = closing_brackets.index(i)
            if (len(stack)>0) and (open_bracets[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                return "unbalanced"
    if len(stack)==0:
        return "the brackets are balanced"
    else:
        return "the brackets are unbalanced"
    

word = "Pneu(monoultrsmicroscopicsilicovolcanoconio)sis"
print (check_brackets(word))
