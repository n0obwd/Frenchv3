from conjugation import *
from database_connection import command


class Verbs:
    def __init__(self,word):
        self.inf = word
        self.conjugation = {1: present, 2: passe_compose, 3: imparfait,
                            4: plus_que_parfait, 5: future_simple, 6: future_anterieur}

    def conjugate(self,word):
        if type(word) is str:
            query = f"SELECT tense_id FROM tenses WHERE tense = \'{word}\'"
            tense_id = command(query, '', '')[0][0]
        else:
            tense_id = word
        print(self.conjugation[tense_id](self.inf))


def game1():
    word = input("What verb do you want to check: ").lower()
    verb = Verbs(word)
    verb.conjugate('présent')


def game2():
    pass


def game3():
    pass


def game4():
    pass