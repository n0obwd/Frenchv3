from conjugation import *
from database_connection import command
from random import randint


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
        return self.conjugation[tense_id](self.inf)


def check_verb():
    word = input("What verb do you want to check: ").lower()
    verb = Verbs(word)
    tense = int(input("What tense?(1-6): "))
    answer = verb.conjugate(tense)
    print(f"Conjugation for {word} is: ")
    for i in range(0,6):
        print(f"{i + 1}. {answer[i]}")
    return [1, 'GG']


def check_vowel(word):
    if word[0].lower() in ['o', 'a', 'e', 'i', 'u', 'é', 'ô']:
        return True
    if word[0].lower() == 'h' and word[1] in ['o', 'a', 'e', 'i', 'u', 'é', 'ô']:
        return True
    return False


def single_answer(entry, ques_col, ans_col, gender_col, score, is_noun):
    question = entry[ques_col]
    correct_ans = entry[ans_col]
    if is_noun:
        if check_vowel(correct_ans):
            article = "l\'"
        else:
            if entry[gender_col] == 'female':
                article = "la "
            else:
                article = "le "
        correct_ans = article + correct_ans
    answer = input(f"{question}: ").lower()
    if correct_ans == answer:
        print("Correct")
        score += 1
    else:
        print("Wrong")
        print(f"Answer: {correct_ans}")
    return score


def multiple_answers(entry, ques_col, gender_col, number_question, correct_ans, **kwargs):
    partial_check = 0
    question = entry[ques_col]
    is_noun = False
    check_plural = False

    print (len(kwargs))
    if len(kwargs) >= 2:
        check_plural = kwargs['check_plural']
    if len(kwargs) >= 1:
        is_noun = kwargs['is_noun']

    for (key, word) in correct_ans.items():
        if is_noun:
            #add article
            if check_plural and correct_ans[key][:-1] == 's' and key == 'country':
                article = 'les '
            else:
                if check_vowel(word):
                    article = "l\'"
                else:
                    if 'female' in key:
                        article = "la "
                    elif 'male' in key:
                        article = "le "
                    elif entry[gender_col] == 'Female':
                        article = "la "
                    else:
                        article = "le "
            correct_ans[key] = article + correct_ans[key]

        #asnwering
        answer = input(f"{question} - {key}: ")
        if answer == correct_ans[key]:
            print("Correct")
            partial_check += 1
        else:
            print("Wrong")
            print(f"Answer: {correct_ans[key]}")
    return partial_check == number_question


def date():
    query = "SELECT * FROM dates"
    dates = command(query, '', '')
    score = 0
    for i in range(0,6):
        entry = dates[randint(0, len(dates) - 1)]
        score = single_answer(entry, 1, 2, 3, score, True)

    score_line = f"Score: {score}/5"
    result = [score == 5, score_line]
    return result


def country():
    num_of_words = int(input("How many words: "))
    query = "SELECT * FROM countries"
    countries = command(query, '', '')
    questions = ['country', 'person(male)', 'person(female)']
    score = 0
    result = []
    for i in range(0, num_of_words):
        entry = countries[randint(0, len(countries) - 1)]
        answers = [entry[1], entry[2], entry[3]]
        correct_ans = dict(zip(questions, answers))
        if multiple_answers(entry, 4, 5, 3, correct_ans, is_noun=True, check_plural=True):
            score += 1

    score_line = f"Score: {score}/{num_of_words}"
    result.append(score == num_of_words)
    result.append(score_line)
    return result


def numbers(number, list):
    #form number from 1 - 999
    if number < 101:
        query = "SELECT num_word FROM numbers WHERE nums = (%s)"
        data = (number,)
        return command(query, data, '')[0][0]
    else:
        num_str = str(number)
        num_dict = dict(list)
        if num_str[0] != 1:
            result = num_dict[int(num_str[0])] + ' cents ' + num_dict[int(num_str[1:])]
            result = result.replace(' zéro', '')
        else:
            result = "cent " + num_dict[int(num_str[1:])]
        return result


def number100():
    result = []
    score = 0
    for _ in range(0,10):
        number = randint(0,100)
        correct_ans = numbers(number, [])
        answer = input(f"{number}: ")
        if answer == correct_ans:
            print("Correct")
            score += 1
        else:
            print("Wrong")
            print(f"{number}: {correct_ans}")
    score_line = f"Score: {score}/10"
    result.append(score == 10)
    result.append(score_line)
    return result


def number1000():
    result = []
    score = 0
    for _ in range(0, 10):
        number = randint(0, 9999999999)
        correct_ans = ''
        if number < 101:
            correct_ans = numbers(number, [])
        else:
            query = "SELECT nums, num_word FROM numbers"
            num_list = command(query, '', '')
            num_str = str(number)
            str_slices = [num_str[-1-i:-4-i:-1][::-1] for i in range(0, len(num_str), 3)]
            addition = [' mille', ' million', ' milliard']
            for i in range(len(str_slices)-1, 0, -1):
                if int(str_slices[i]) == 0:
                    continue
                correct_ans = correct_ans + " " + numbers(int(str_slices[i]), num_list) + addition[i - len(str_slices) + 3]
                if int(str_slices[i]) > 1 and addition[i - len(str_slices) + 3] != ' mille':
                    correct_ans = correct_ans + 's'
            correct_ans = correct_ans + " " + numbers(int(str_slices[0]), num_list)
        correct_ans = correct_ans[1:]
        if 'un mille' in correct_ans and not 'et un mille' in correct_ans:
            correct_ans = correct_ans.replace('un mille', 'mille')
        answer = input(f"{number}: ")
        if answer == correct_ans:
            print("Correct")
            score += 1
        else:
            print("Wrong")
            print(f"{number}: {correct_ans}")
    score_line = f"Score: {score}/10"
    result.append(score == 10)
    result.append(score_line)
    return result
