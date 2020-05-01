from database_connection import command
from game_list import *


class Games:
    def __init__(self, mode):
        self.game_mode = mode
        self.game_list = {1: check_verb, 15: date, 20: country, 10: number100, 11:number1000}
        self.result = []

    def calling_game(self):
        while True:
            self.result = self.game_list[self.game_mode]()
            print(self.result[1])
            if not self.rerun():
                break

    def rerun(self):
        is_rerun = input("Practice again? (Y\\N): ").lower()
        return is_rerun == 'y'


def is_break():
    again = input("Different practice? (Y\\N): ").lower()
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
        game.calling_game()
        if is_break():
            break
    print("Thank you.")
