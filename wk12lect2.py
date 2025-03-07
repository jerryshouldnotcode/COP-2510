#wk 12 lecture2

#multiple inheritance example


#parent classes
class Animal:
    def __init__(self, name):
        print(f'{name} is an animal.')
        super().__init__(name)


class CannotFly:
    def __init__(self, name):
        print(f'{name} cannot fly.')
        super().__init__(name)
        
class LikestoHunt:
    def __init__(self, name):
        print(f'{name} likes to hunt.')
        #last parent doesn't get the super reference

#child class

class Cat(Animal, CannotFly, LikestoHunt):
    def __init__(self,name):
        print(f"I'm a cat named {name}.")
        super().__init__(name) #super reference                     

class Rat(Animal, CannotFly):
    def __init__(self,name):
        print(f" I'm a rat named {name}.")
        super().__init__(name)

#main portion
#kitty = Cat('Pandemica')
#mouse = Rat('Jerry')



#protected status for attributes
class Shape:
    def __init__(self,l,w):
        self._length = l  #_means attribute is protected (inbetween __ and _)
        self._width = w

    def __str__(self):
        return f'Length:{self._length}, width:{self._width}'

class Rectangle(Shape):
    def __init__(self,l,w):
        Shape.__init__(self,l,w)

    def setlength(self,l):
        self._length = l

    def setwidth(self,w):
        self._width = w

    #no accessor class needed for the child to access data elements
    
    def area(self):
        print(f'Area is {self._length * self._width}')


#main portion

rec_1 = Rectangle(10,20)
rec_1.area()
print(rec_1)

shape_1 = Shape(50,20)
print(shape_1)
#shape_1.area() - won't work; parent can't access the child method


#polymorphism - ability for a component to take different forms based on the object it is working with
#e.g the + symbol - addition for int, float   ; concatenation for strings (prevents operator overloading, function overloading)

#Example 1: polymorphism in built-in functions
print(len('3 more weeks')
print(len[10,34,52,45])


#Example 2: polymorphism in user-defined functions
def add(x,y,z=0):
    return x + y + z

print(add(2,3))
print(add(5,3,4))


#Example 3: polymorphism in classes (via methods)



#Example 4: polymorphism in inheritance
        
