# Document at least 3 use cases of instance methods


# example 1
class Clothing:
    
    def __init__(self, color, size, style, price):
        self.color = color
        self.size = size
        self.style = style
        self.price = price
    
    # instance method
    def change_price(self, price):
        self.price = price
   
   
# example 2      
class Dog:
    
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    # instance method
    def change_age(self, age):
        self.age = age


# example 3
class Drinks:
    
    breakable = True
    
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        
    # instance class
    def change_size(self, size):
        self.size = size
        
coke = Drinks("cola cola", "small")
print(coke.size)

coke.change_size("big")
print(coke.size)
