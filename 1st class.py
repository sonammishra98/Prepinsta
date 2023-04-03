class employee:
    id=10
    Name="john"
    def display(self):
        id=self.id
        name=self.Name
        print("Id:%d\nName:%s"%(self.id,self.Name))
emp=employee()
emp.display()