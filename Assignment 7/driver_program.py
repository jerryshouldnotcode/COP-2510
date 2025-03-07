'''
Name: Jeremiah Adeyemi
U-Number: U58971672
Description: creating the driver Program, the main module needed for the Trivia Game.
'''
import questions_class
from trivia_questions import triv

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = 0  # Start with the first player

    def switch_player(self):
        self.current_player = 1 - self.current_player  # Switch between 0 and 1

    def play(self):
        triv()
        for question in triv():
            current_player = self.players[self.current_player]
            answer = current_player.answer_question(question)
            
            if answer == question.answer:
                print(f"Correct! {current_player.name} gets a point.")
                current_player.increment_score()
            else:
                print(f"Wrong! The correct answer was: {question.answer}")

            self.switch_player()

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

    def answer_question(self, question):
        print(f"{self.name}, here is your question:")
        print(question)
        for i, option in enumerate(question.options, 1):
            print(f"{i}. {option}")

        return input("Your answer: ")

    def increment_score(self):
        self.score += 1

# Example usage:
player1 = Player("Player 1")
player2 = Player("Player 2")

game = Game(player1, player2)
game.play()

print(f"\nFinal Scores:")
print(f"{player1.name}: {player1.score} points")
print(f"{player2.name}: {player2.score} points")





    


