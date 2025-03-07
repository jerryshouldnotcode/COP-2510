class Student:

    def __init__(self, fname, lname, school, year):
        self.__fname = fname
        self.__lname = lname
        self.school = school
        self.year = year

    def introduce(self):
        print(f'My name is {self.__fname}, and I study at {self.school}')
        print(f'I am a {self.year} student.')
        print('Nice to meet you!')
        
    
Jeremiah = Student('Jeremiah','Adeyemi', 'USF', 'Sophomore')

Jeremiah.introduce()
