# Document at least 3 use cases of class methods

# use cases of classmethods are 
# 1. classmethods are used when some attributes of a 
#    class are known and don't want to be changed
# 2. classmethods can help us define some functions we can manipulate
# 3. classmethod can be used to group element of same type in a class
# 4. Classmethods can be used to update/change the class attributes

 
from datetime import date 
  
class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
      
    @classmethod
    def dob(cls, name, year): 
        return cls(name, date.today().year - year) 
      
# person1 = Person('kings', 21) 
# person2 = Person.dob('kc', 1996) 
  
# print (person1.age) 
# print (person2.age) 
# print (person2.name) 

class Vehicle:
    wheels = 4
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    @classmethod
    def change_no_wheels(cls, type, change_wheels):
        return cls(type, 'wheels')
    
keke = Vehicle('keke', 'yellow')
keke.change_no_wheels("triCycle", 3)

print(keke.change_no_wheels)



class Building:
    def __init__(self, type, color):
        self.type = type
        self.color = color
        
    @classmethod
    def change_color(cls, color):
        return cls(color)

        