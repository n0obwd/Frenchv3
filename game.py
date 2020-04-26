from database_connection import command


class Games():
    def __init__(self, mode):
        self.game_mode = mode
        self.game_list = {1: game1, 2: game2, 3: game3, 4: game4}
        self.startgame(self.game_mode)

    def startgame(self,mode):
        self.game_list[mode]()


class Verbs():
    def __init__(self,word):
        self.inf = word
        self.conjugation = {1: present, 2: passe_compose, 3: imparfait,
                            4: plus_que_parfait, 5: future_simple, 6: future_anterieur}

    def conjugate(self,word):
        if type(word) is str:
            command_str = f"SELECT tense_id FROM tenses WHERE tense = \'{word}\'"
            tense_id = command(command_str, '')[0][0]
        else:
            tense_id = word
        print(self.conjugation[tense_id](self.inf))

def vowel(word):
    pass

def present(verb):
    command_str = f"SELECT inf,present1,present2,present3,present4,present5,present6 FROM verb WHERE inf = \'{verb}\'"
    conj_v = command(command_str, '')
    #command_str = f"SELECT * FROM verb WHERE inf = \'{verb}\'"
    #conj_v = command(command_str, '')
    result = conj_v
    return result

def passe_compose():
    pass


def imparfait():
    pass


def plus_que_parfait():
    pass


def future_simple():
    pass


def future_anterieur():
    pass


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



def display_menu():
    print("Welcome to budget French practice")
    print("Available exercise:")
    print("----------------")
    print("Verb: ")
    print("1/ Check conjugation of a verb")
    print("2/ Test conjugation of a verb in specific tense")
    print("3/ Test conjugation of random verbs (infinitive")
    print("4/ Test conjugation of random verbs (random tense")
    print("----------------")


if __name__ == '__main__':
    display_menu()
    action = int(input("Choose your action: "))
    game = Games(action)
