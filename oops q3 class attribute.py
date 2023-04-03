class student:
    sccount=0
    def __init__(self,age,name,id,roll):
      self.age=age
      self.id=id
      self.name=name
      self.roll=roll
      student.sccount +=1
    def display(self):
       print("total emp is %d"%student.sccount)
    def display1(self):
       print("name :", self.name ,"age:", self.age)
    
sc1=student(10,'rahul',222,1)
sc2=student(11,'rohan',234,12)
sc3=student(13,'rupal',235,14)
sc1.display1()
sc2.display1()
sc3.display1()
print("total emp is %d"%student.sccount)
#add,remove,modify attributes in classes
getattr(sc1,'age')
sc1.display1()
hasattr(sc1,'age')
sc1.display1()
setattr(sc1,'age',8)
sc1.display1()
#delattr(sc1,'age')

#built in attributes in classes
print("student doc",student .__doc__)
print("student name",student.__name__)
print("student base",student.__base__)
print("student module:",student.__module__)
print("student dict:",student.__dict__)

