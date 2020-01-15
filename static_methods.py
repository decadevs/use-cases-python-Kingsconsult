# Document at least 3 use cases of static methods

# This method don't rely on the class attributes
# They are completely independent of everythin around them

# example 1
class Shape:
    def __init__(self, name):
        self.radius = name
        
    @staticmethod
    def calc_sum_of_angle(n):
        return (2 * n - 4) * 90
    
a = Shape("triangle")
print(a.calc_sum_of_angle(4))

# example 2
class Vehicle:
    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def fuel_consumed(num):
        return num * 5
    
lexuz = Vehicle("lexuz")

print(lexuz.fuel_consumed(6))


# example 3
class Building:
    def __init__(self, type, color):
        self.type = type
        self.color = color
        
    @staticmethod
    def number_of_occupants(a):
        return a * 6
    
decagon = Building("storey Building", "brown")
print(decagon.number_of_occupants(3))
