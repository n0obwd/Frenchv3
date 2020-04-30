from database_connection import command
from random import randint


def load_pronouns():
    query = f"SELECT * FROM subject_pronouns"
    sp_list = list(command(query, '', ''))
    return sp_list


def vowel(verb):
    vowel_list = ['o', 'a', 'e', 'i', 'u', 'é']
    return verb[0] in vowel_list or (verb[0:2] == 's\'' and verb[2] in vowel_list)


def reflective(verb):
    return verb[0:2] in ["se", "s\'"]


def present(verb):
    query = "SELECT present1,present2,present3,present4,present5,present6,is_reflective FROM verbs WHERE inf = (%s)"
    data = (verb, )
    conjugated_verb = command(query, data, '')[0]
    sp = load_pronouns()
    conj_list = []
    sp_col = 2
    if conjugated_verb[6]:
        for i in range(0,8):
            sp[i] = list(sp[i])
            sp[i][4] = sp[i][2] + ' ' + sp[i][4]
            sp[i][5] = sp[i][2] + ' ' + sp[i][5]
        if vowel(verb):
            sp_col = 5
        else:
            sp_col = 4
    for i in range(0, 6):
        if i == 0:
            if vowel(verb) and not conjugated_verb[6]:
                conj_list.append('j\'' + conjugated_verb[i])
            else:
                conj_list.append(sp[i][sp_col] + ' ' + conjugated_verb[i])
        if i == 1:
            conj_list.append(sp[i][sp_col] + ' ' + conjugated_verb[i])
        if i == 2:
            conj_list.append(sp[i + randint(0, 1)][sp_col] + ' ' + conjugated_verb[i])
        if 2 < i < 5:
            conj_list.append(sp[i+1][sp_col] + ' ' + conjugated_verb[i])
        if i == 5:
            conj_list.append(sp[i + randint(1, 2)][sp_col] + ' ' + conjugated_verb[i])
        if conj_list[i].count(' ') > 1:
            conj_list[i] = ''.join(conj_list[i].rsplit(" ", 1))
    return conj_list


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
