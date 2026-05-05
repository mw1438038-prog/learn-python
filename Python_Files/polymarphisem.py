
# Ploy: Many
# morphism: Shapes
 
class Dog():
 
   def __init__(self,name):
      self.name =name
 
   def speak(self):
      return self.name + ' Says Whuuuuuff'
 
 
class Cat():
 
   def __init__(self, name):
      self.name = name
 
   def speak(self):
      return self.name + ' Says Meeeeeeooooo'
 
my_tommy = Dog('Tommy')
 
my_sally = Cat('Sally')
 
print(my_sally.speak())
print(my_tommy.speak())
 
print('x'*20)
# with foor loop
for pet in [my_sally,my_tommy]:
   print(pet.speak())
 
print('x'*20)
# with Function
 
def my_pet_speak(pet):
   print(pet.speak())
my_pet_speak(my_tommy)
my_pet_speak(my_sally)
 
 