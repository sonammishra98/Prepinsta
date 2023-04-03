class student:
    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age
    def display(self):
            print("%d %s"%(self.id,self.name))
sc1=student(101,'rahul',10)
sc2=student(102,'vihan',11)
sc1.display()
sc2.display()