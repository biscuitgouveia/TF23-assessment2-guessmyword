import random

all_words = open("word-bank/all_words.txt")

def choose_word(word_list):
    target_words = open("word-bank/target_words.txt")
    target_words_list = target_words.readlines()
    return random.choice(target_words_list)

# TODO: Find a way to handle double letters

'''
def score_word(guess_word, target_word):
    score_string = str()
    target_frequency = dict()
    guess_frequency = dict()

    for letter in target_word:
        if letter not in target_frequency:
            target_frequency[letter] = 1
        else:
            target_frequency[letter] += 1

    for letter in guess_word:
        guess_frequency[letter] = 0

    for counter, letter in enumerate(guess_word):
        guess_frequency[letter] += 1
        if letter == target_word[counter] and guess_frequency[letter] <= target_frequency[letter]:
            score_string += "\033[0;32m" + letter
        elif letter in target_word and guess_frequency[letter] <= target_frequency[letter]:
            score_string += "\033[1;33m" + letter
        else:
            score_string += "\033[1;37m" + letter
    return score_string
'''

def score_word(guess_word, target_word):

    score_string = str()
    score_list = list()
    target_frequency = dict()
    guess_frequency = dict()
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    white = "\033[0;37m"

    for letter in guess_word:
        score_list.append((letter, white))

    for letter in target_word:
        if letter not in target_frequency:
            target_frequency[letter] = 1
        else:
            target_frequency[letter] += 1

    for letter in guess_word:
        guess_frequency[letter] = 0

    for counter, letter in enumerate(guess_word):
        if letter == target_word[counter]:
            guess_frequency[letter] += 1
            score_list[counter] = (letter, green)

    for counter, letter in enumerate(guess_word):
        if score_list[counter][1] == green:
            continue
        else:
            guess_frequency[letter] += 1
        if letter in target_word and guess_frequency[letter] <= target_frequency[letter]:
            score_list[counter] = (letter, yellow)
        else:
            score_list[counter] = (letter, white)

    for letter in score_list:
        score_string += letter[1] + letter[0]

    return score_string



current_word = (choose_word("word-bank/all_words.txt"))
print(current_word)
print(score_word("hello", current_word))