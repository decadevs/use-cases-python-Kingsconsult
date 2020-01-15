# Document 1 use case of an interface in python
# That is define an interface using the abstract base class module
# Add at least 3 entities that can implement the interface in a way that make sense.


# an interface is a set of publicly accessible methods on an object
# which can be used by other parts of the program to interact with that object

# Interfaces set clear boundaries and help us organize our code better
# Interfaces are abstract classes that implements all methods in a class

# Use case

class Employee:
    
    def __init__(self, name, level):
        self.name = name
        self.level = level
        
    