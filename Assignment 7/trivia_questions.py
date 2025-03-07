'''
Name: Jeremiah Adeyemi
U-Number: U58971672
Description: creating a trivia questions module, a module needed for the Trivia Game.
'''

from questions_class import QU

def triv():
    question_1 = QU('How many days are in a lunar year?', ['354', '365','243','379'], '354')
    question_2 = QU('What is the largest planet?', ['Mars', 'Jupiter', 'Earth', 'Pluto'], 'Jupiter')
    question_3 = QU('What is the largest kind of whale?',['Orca whale', 'Humpback whale', 'Beluga whale','Blue whale'],'Blue whale')
    question_4 = QU('Which dinosaur could fly?',['Triceratops','Tyrannosaurus Rex', 'Pteranodon','Diplodocus'],'Pteranodon')
    question_5 = QU('Which of these Winnie the Pooh characters is a donkey?', ['Pooh','Eeyore','Piglet','Kanga'], 'Eeyore')
    question_6 = QU('What is the hottest planet?', ['Mars','Pluto','Earth','Venus'],'Venus')
    question_7 = QU('Which dinosaur had the largest brain compared to body size?', ['Trodon','Stegosaurus','Ichthyosaurus','Gigantoraptor'],'Trodon')
    question_8 = QU('What is the largest type of penguins?',['Chinstrap penguins','Macaroni penguins','Emperor penguins','White-flippered penguins'],'Emperor Penguins')
    question_9 = QU('Which children\'s story character is a monkey?',['Winnie the Pooh','Curious George','Horton','Goofy'],'Curious George')
    question_10 = QU('How long is a year on Mars?',['550 Earth days','498 Earth days','126 Earth days','687 Earth days'],'550 Earth days')

    questList = [question_1,question_2,question_3,question_4,question_5,question_6,question_7,question_8,question_9,question_10]
    return questList
