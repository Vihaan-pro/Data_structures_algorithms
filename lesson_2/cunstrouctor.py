class Family():
    def __init__(self,name,age,hight,relation):
       self.name = name
       self.age = age
       self.hight = hight
       self.relation = relation

    def traveling(self):
     print(self.name,"is going to the zoo")
     


        
    def eating(self):
     print("is having a meal together")


person1 = Family("arshi",35,178,"auntie") 
person2 = Family("vivek",32,182,"uncle")
person1.traveling()
person2.traveling()