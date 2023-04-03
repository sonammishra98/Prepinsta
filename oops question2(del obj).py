#given program will throw an attribute error

class member:
    name='john'
    age=10
    p_no=980834
    address="kol"
    salary=10000
    def printsalary(sonam):
      print("age:%d salary:%d"%(sonam.age,sonam.salary))

mem=member()
mem.printsalary()
del mem.age
mem.printsalary()
