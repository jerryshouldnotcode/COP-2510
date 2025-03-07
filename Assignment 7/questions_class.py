'''
Name: Jeremiah Adeyemi
U-Number: U58971672
Description: creating a questions class, a module needed for the Trivia Game.
'''

#questions_class.py

class QU:
    def __init__(self,trivia, options, answer):
        self.__trivia = trivia
        self.__options = options
        self.__answer = answer
    
    def __str__(self):
        result = (f'Question: {self.__trivia}\n')
        for count, ele in enumerate(self.options,1):
            result += f'{count}. {ele}\n'  
        return result            

              
             
    
    
    
    
