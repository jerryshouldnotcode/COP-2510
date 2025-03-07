class Person:
    def __init__(self, name, sex, age):
        self.__name = name
        self.__sex = sex
        self.__age = age

    def __str__(self):
        return(f'This is {self.__name}!\
                  \n{self.__name} is a {self.__sex}\
                  \n{self.__name} is {self.__age} years old')

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Mother(Person):
    def __init__(self, name, sex, age):
        #Person.__init__(self, name, sex, age) #explicit call
        super().__init__(name,sex,age) #remember, super 'method'
        self.title = 'Mum'

    def get_title(self):
        return self.title


mum1 = Mother('Lady Macbeth', 'Female', '43')
print(mum1)
print(mum1.get_title())
print(mum1.title)
        
        
        
