from database_connection import command
from game_list import *


class Games:
    def __init__(self, mode):
        self.game_mode = mode
        choice = list(range(1,14))
        game_name = ['game'for i in choice ]
        self.game_list = {1: game1, 2: game2, 3: game3, 4: game4}
        self.start_game(self.game_mode)

    def start_game(self,mode):
        self.game_list[mode]()


def isbreak(self):
    again = input("Do you want to play again? (Y\\N): ").lower()
    return again == 'n'


class Words:
    def __init__(self):
        pass


def display_menu():
    print("Welcome to budget French practice")
    print("Available exercise:")
    print("----------------")
    print("Verb: ")
    print("1/ Check conjugation of a verb")
    print("2/ Test conjugation of a verb in specific tense")
    print("3/ Test conjugation of random verbs (infinitive)")
    print("4/ Test conjugation of random verbs (random tense)")
    print("----------------")
    print("Number: ")
    print("10/ Random number 1 - 100")
    print("11/ Random number 1 - 1000++")
    print("----------------")
    print("Date: ")
    print("15/ Random date vocabulary")
    print("----------------")
    print("Country: ")
    print("20/ Random country")
    print("----------------")


if __name__ == '__main__':
    while True:
        display_menu()
        action = int(input("Choose your action: "))
        game = Games(action)
        if isbreak():
            break
    print("Thank you.")
