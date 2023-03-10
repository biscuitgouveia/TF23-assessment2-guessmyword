import random

MAX_TRIES = 6
TARGET_WORDS = open("word-bank/all_words.txt")
VALID_WORDS = open("word-bank/target_words.txt")
attempts = 0
game_state = "in_game"

def choose_word(word_list):
    valid_words_list = word_list.readlines()
    target_word = random.choice(valid_words_list)
    return random.choice(target_word)

# TODO: Simplify the scoring algorithm. It works, but it's a bit convoluted

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
            continu
        else:
            guess_frequency[letter] += 1
        if letter in target_word and guess_frequency[letter] <= target_frequency[letter]:
            score_list[counter] = (letter, yellow)
        else:
            score_list[counter] = (letter, white)

    for letter in score_list:
        score_string += letter[1] + letter[0]

    return score_string

def validate_word(guess_word):
    if len(guess_word) < 5:
        return "Invalid - Not enough letters. Please enter a five letter English word: "
    elif len(guess_word):
        return "Invalid - Too many letters. Please enter a five letter English word: "
    elif word not in ALL_WORDS.readlines():
        return "Invalid - Word not found in the dictionary. Please try again: "
    elif guess_word == target_word:
        return "win"
    else:
        return True

target_word = choose_word("word-bank/target_words.txt")
guess_word = input("Type a five letter English word and press enter: ")

while game_state == in_game:
