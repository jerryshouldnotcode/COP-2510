'''
Name: Jeremiah Adeyemi
U-Number: U58971672
Description: using OOP concepts to create an area and perimeter calculator that works
            for any n-sided polygon.

'''

#n_sided_polygon.py

from math import pi, tan

class Polygon:

    def __init__(self,numsides,length):
        self.__numsides = numsides
        self.__length = length
        
        
    def get_numsides(self):             #getter methods
        return self.__numsides

    def get_length(self):
        return self.__length

    
    def update_numsides(self, n):       #setter methods
        self.__numsides = n

    def update_length(self, s):
        self.__length = s

    #area and perimeter methods
        
    def peri(self):
        return self.get_numsides() * self.get_length()
        
    def area(self):
        num_sides = self.get_numsides()
        length_squared = self.get_length() ** 2
        tan_value = tan(pi / num_sides)
        return (num_sides * length_squared) / (4 * tan_value)
    
def main():
    n = int(input('Enter number of sides(>=3): '))

    while n < 3:
        print('Invalid input. ',end='')
        n = int(input('Re-enter the number of sides(>=3): '))
        
    s = float(input('Enter length of each side(>=0.1): '))

    while s < 0.1:
        print('Invalid input. ',end='')
        s = float(input('Re-enter length of each side(>=0.1): '))

    polygon_1 = Polygon(n,s)
   
    print(f'The number of sides of the polygon is {polygon_1.get_numsides()} and each side is of length {polygon_1.get_length()} units.')
    print(f'The perimeter of the polygon is {polygon_1.peri():.3f} units and its area is {polygon_1.area():.3f} square units.')
        
        
main()
  
