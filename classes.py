# class Point : 
#     def __init__(self, x, y): 
#         self.x = x 
#         self.y = y

#     def move(self): 
#         print ("move")

#     def draw(self): 
#         print('draw')


# point1 = Point(10, 20 )
# # print(point1.x)

# class Person : 
#     def __init__(self, name): 
#         self.name = name
    
#     def talk(self) : 
#         print(f"Hello I am {self.name}")

# person1 = Person("Julian")
# # print(person1.name)
# person1.talk()

# class Mammal : 
#     def walk(self) : 
#         print("walk")

# class Dog(Mammal) : 
#     pass

# class Cat(Mammal) : 
#     pass

# dog1 = Dog()
# dog1.walk()
    

import converter
from converter import kgToLbs  ## specific function 

kgToLbs(100)

print(converter.kgToLbs(70))


# def findMax (arr) : 
#   max = arr[0]
#   for x in arr: 
#     if x > max: 
#       max = x 
#   return max 

def findMin (arr) : 
    min = arr[0]
    for x in arr: 
        if x < min:
            min = x
  
  return min

