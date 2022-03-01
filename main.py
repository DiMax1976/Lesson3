nums_tr = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
           'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}


def num_translate(nums_tr, word_eng: str) -> str:
    """Translate english number to russian _ lesson1, task 1+2 additionaly"""
    tags = 0
    # print(nums_tr)
    if word_eng.istitle() == True:
        tags = 1
    word_eng = word_eng.lower()
    for key, value in nums_tr.items():
        if key == word_eng:
            if tags == 1:
                return f"\"{value.capitalize()}\""  # Точно не уверен нужно было делать кавычки но в задании есть коавычки
            else:
                return f"\"{value.lower()}\""


# help(num_translate)
print("Task1 + Task2 additionaly")
print("_" * 105)
print('\n')
print(num_translate(nums_tr, word_eng="one"))
print(num_translate(nums_tr, word_eng="two"))
print(num_translate(nums_tr, word_eng="three"))
print(num_translate(nums_tr, word_eng="four"))
print(num_translate(nums_tr, word_eng="five"))
print(num_translate(nums_tr, word_eng="eight"))
print(num_translate(nums_tr, word_eng="nine"))
print(num_translate(nums_tr, word_eng="eleven"))
print(num_translate(nums_tr, word_eng="One"))
print(num_translate(nums_tr, word_eng="Six"))
print("_" * 105)
print('\n')
print("Task 3:")
print('\n')

NamesStaff = ["Иван", "Мария", "Петр", "Илья", "Иисус",
              "Антон"]  # - так проще и короче и хоть сколько имён можно вставлять!
Dict_n = {}

print(NamesStaff)
print('\n')


def theraurus1(Dict_n, NameSt: list):  # Проще сразу список с Именами
    for elem in range(len(NameSt)):  # Проверяем список
        NamesS = NameSt[elem]
        if NamesS[0] in Dict_n:  # Проверяем наличие ключа!
            Dict_n[NamesS[0]].append(NameSt[elem])
        else:
            Dict_n[NamesS[0]] = [NameSt[elem]]
    print(Dict_n)


def theraurus(NameSt1, NameSt2, NameSt3, NameSt4):  # Как в задании - скучно так делать
    Dict_n_ = {}
    if NameSt1[0] in Dict_n_:  # Проверяем наличие ключа!
        Dict_n_[NameSt1[0]].append(NameSt1)
    else:
        Dict_n_[NameSt1[0]] = [NameSt1]
    if NameSt2[0] in Dict_n_:  # Проверяем наличие ключа!
        Dict_n_[NameSt2[0]].append(NameSt2)
    else:
        Dict_n_[NameSt2[0]] = [NameSt2]
    if NameSt3[0] in Dict_n_:  # Проверяем наличие ключа!
        Dict_n_[NameSt3[0]].append(NameSt3)
    else:
        Dict_n_[NameSt3[0]] = [NameSt3]
    if NameSt4[0] in Dict_n_:  # Проверяем наличие ключа!
        Dict_n_[NameSt4[0]].append(NameSt4)
    else:
        Dict_n_[NameSt4[0]] = [NameSt4]
    print(Dict_n_)  # Выводим результат!


def theraurus_2(*args):  # *args еще вариант
    Dict_n2 = {}
    for elem in args:
        if elem[0] in Dict_n2:  # Проверяем наличие ключа!
            Dict_n2[elem[0]].append(elem)
        else:
            Dict_n2[elem[0]] = [elem]
    print(Dict_n2)
    print("_" * 105)


theraurus1(Dict_n, NamesStaff)
theraurus("Иван", "Мария", "Петр", "Илья")
print("_" * 105)
theraurus_2("Иван", "Мария", "Петр", "Илья")
theraurus_2("Иван", "Мария", "Петр", "Илья", "Иисус", "Ильдус", "Антон", "Али-Баба", "Оюшминальд",
            "Арчибальд")  # для тренировки
print("Task 4: It's so boring Task! I woud't to make ")
print("_" * 105)
print('\n')
print("Task 5: Joke Mashine!")
print('\n')

import random


def get_jokes(Number):
    """To make random jokeTo make random joke additional function - генератор шуточных выражений
    даеются списки слов - существительное, время и прилагательное
    в функцию передается количество шуток

    for elem in range(Number): цикл
    в который передается выбор случайных слов:
    random.choice(nouns)
    random.choice(adverbs)
    random.choice(adjectives)

    joke_list.append(elems_list) - добавляются выражения в список"""

    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    for elem in range(Number):
        elems_list = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
        joke_list.append(elems_list)
    print(joke_list)


def get_jokes1(Number):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    joke_list = []
    flag = 0
    for elem in range(Number):
        # поиск повтора
        if flag == 0:
            joke_word1 = random.choice(nouns)
            joke_word2 = random.choice(adverbs)
            joke_word3 = random.choice(adjectives)
            flag = 1
        else:
            joke_word1 = random.choice(nouns)
            joke_word2 = random.choice(adverbs)
            joke_word3 = random.choice(adjectives)
            flag = 1
        elems_list = f'{joke_word1} {joke_word2} {joke_word3}'
        joke_list.append(elems_list)
    print(joke_list)


# Кол-во шуток! - 2
get_jokes(6)

print("_" * 155)
print("End homework of lesson 3!")
print("_" * 105)
help(get_jokes)