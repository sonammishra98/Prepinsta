#inheritance : single level
class animal:
    def speak(self):
        print("barking")
class dog(animal):
    def eat(self):
        print("eating")
class cat(animal):
    def sleep(self):
        print("sleeping")
c=cat()
c.sleep()
c.speak()

#multilevel inheritance
class animal:
    def speak(self):
        print("barking")
class dog(animal):
    def eat(self):
        print("eating")
class cat(dog):
    def sleep(self):
        print("sleeping")
c=cat()
c.sleep()
c.speak()
c.eat()

#multiple class:inheritance
class solution:
    def add(self ,a,b):
        return a+b
class solution1(solution):
    def mul(self,a,b):
        return a*b
class solution3(solution1,solution):
    def divide(self,a,b):
        return a/b
s=solution3()
print("addition is:",s.add(10,20))
print("multiplication is:",s.mul(10,20))
print("division is:",s.divide(10,20))

print(issubclass(solution1,solution)) #to cheak if class a is subclass of b or not
print(isinstance(s,solution1)) #method is used to check the relationship between the objects and classes. It returns true if the first parameter, i.e., obj 
                               #is the instance of the second parameter, i.e., class

                               