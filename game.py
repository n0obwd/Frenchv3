
class Games():
    def __init__(self, mode):
        self.game_mode = mode
        self.game_list = {1: game1, 2: game2, 3: game3, 4: game4}
        self.startgame(self.game_mode)

    def startgame(self,mode):
        self.game_list[mode]()


def game1():
    word = input("What verb do you want to check: ").lower()
    print(word)


def game2():
    pass


def game3():
    pass


def game4():
    pass


def conjugation(verb, tense):
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
