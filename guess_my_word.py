#!/usr/bin/env python3
"""
Guess-My-Word is a game where the player has to guess a word.
<your description> 
Author: Ethan Gouveia
Delivery: North Metropolitan TAFE, Unit ICTPRG302, Assessment 2
"""

import random
import logging

MAX_ATTEMPTS = 6
WORD_LENGTH = 5

ALL_WORDS = 'word-bank/all_words.txt'
TARGET_WORDS = 'word-bank/target_words.txt'
LETTERS_STRING = "QWERTYUIOPASDFGHJKLZXCVBNM"


def generate_letters(letters_input=LETTERS_STRING):
    """Generate a dictionary of all the letters in the English
    language with their values set as 1. Used with format_remaining_letters
    to generate a keyboard display of previously guessed letters.

    :param letters_input: string of all letters in the English language
    :return: letter_dictionary: A dictionary of all letters in the English language with the letters as the keys and 1 as the values
    """

    letter_dictionary = dict()

    for letter in letters_input:
        letter_dictionary[letter] = 1

    return letter_dictionary


def format_remaining_letters(letter_dictionary, score, guess):
    """Prepare display of all the letters on the keyboard, formatted as black if
    they're viable for guesses, red if they've been ruled out, yellow if they're
    in the wrong spot, and green if they're the correct letter in the right spot

    :param letter_dictionary: dictionary of letters with their values as 1 if ruled out of the game, and 0 otherwise
    :param score: a tuple of each letter's score, returned from the score_guess function
    :param guess: the current player guess
    :return: a tuple containing the updated letter_dictionary and a formatted string of letters
    """

    BLACK = "\033[0;40m"
    RED = "\033[0;101m"
    GREEN = "\033[0;42m"
    YELLOW = "\033[0;43m"
    RESET = "\033[m"

    remaining_letters_string = BLACK + ' '

    if score == None:
        score = (4, 4, 4, 4, 4)

    for counter, letter_score in enumerate(score):
        if letter_dictionary[guess[counter].upper()] < 2:
            if letter_score == 2:
                letter_dictionary[guess[counter].upper()] = 3
            elif letter_score == 1:
                letter_dictionary[guess[counter].upper()] = 2
            elif letter_score == 0:
                letter_dictionary[guess[counter].upper()] = 0
            elif letter_score == 4:
                letter_dictionary[guess[counter].upper()] = 1

    for letter, value in letter_dictionary.items():
        if letter == 'A':
            remaining_letters_string += RESET + '\n ' + BLACK + ' '
        elif letter == 'Z':
            remaining_letters_string += RESET + '\n   ' + BLACK + ' '

        if value == 0:
            remaining_letters_string += RED + letter + BLACK + ' '
        elif value == 1:
            remaining_letters_string += BLACK + letter + BLACK + ' '
        elif value == 2:
            remaining_letters_string += YELLOW + letter + BLACK + ' '
        elif value == 3:
            remaining_letters_string += GREEN + letter + BLACK + ' '

    remaining_letters_string += RESET

    return (letter_dictionary, remaining_letters_string)


def give_feedback(score, turns_taken):
    """Code to give dynamic feedback based on how well the player has scored

    :param score: tuple of the current score
    :param turns_taken: int of the number of turns currently played
    :return: string to print out to the player as feedback for their turn
    """
    feedback_abysmal_guess = ["No dice... let's try again",
                     "Well, at least now you know what letters NOT to use!",
                     "I know, I know, it happens. I believe in you!",
                     "Even I guess completely wrong sometimes. Such is the beauty of random choice",
                     "Oh no! I'm so sorry, what a bummer!",
                     "Swing and a miss!",
                     "...No",
                     "Are you having fun? I'm having fun. Luckily having fun is all that matters",
                     "Well it's only the first try. It's bound to happen at some point",
                     "ABSOLUTELY NOT. That is incorrect!",
                     "It's like Benjamin Franklin said: 'I didn’t fail the test. I just found 100 ways to do it wrong.",
                     "I feel like it's not your day today, my friend"]
    feedback_standard_early_game = ["Solid start!",
                                    "Nice",
                                    "Good pace, slow and steady. Don't mess it up",
                                    "Good start! Onward and upward!",
                                    "Nice one, keep it up!"]
    feedback_excellent_early_game = ["Are you a wizard or something?",
                                     "Looks like you don't mess around!",
                                     "Okay, okay, no need to show off so early",
                                     "Beginner's Luck? No, there's no way you're a beginner",
                                     "Look at you go! I'd be impressed if this weren't based on random chance!"]
    feedback_halfway_there = ["You're halfway there!",
                              "The hard part is over, time to fill in the gaps!",
                              "You've made it this far, not long to go now!",
                              "Keep at it, you're more than halfway there!",
                              "Don't mess it up now, you're getting close!"]
    feedback_unlikely_win = ["I'll be honest, I don't like your chances... but you can't give up now! Do your best!",
                             "No chance you'll get this, prove me wrong",
                             "You've done your best, but it's not paid off yet. Give it your best shot!",
                             "Are you frustrated? You should be frustrated",
                             "If you feel bad about this, just remember that you get to continue with your day\nand I'll be reduced to digital oblivion as soon as you sign out"]
    feedback_close_win = ["This isn't your first rodeo, is it?",
                          "Almost there! Get it over the line!",
                          "You're a natural at this, finish it off!",
                          "Don't let me get in your way, you're so close!",
                          "Impressive. Don't disappoint me now"]
    feedback_close_call = ["It's your last chance now, do your best!",
                           "Last chance to get it!",
                           "So close yet so far, do your best!",
                           "I believe in you, take your best shot!",
                           "It's gonna be a close call!"]

    if score == (0, 0, 0, 0, 0):
       return random.choice(feedback_abysmal_guess)
    elif score.count(2) == 3:
        return random.choice(feedback_halfway_there)
    elif (score.count(2) < 3 or score.count(1) < 4) and turns_taken < 3:
        return random.choice(feedback_standard_early_game)
    elif (score.count(2) > 2 or score.count(1) > 3) and turns_taken < 3:
        return random.choice(feedback_excellent_early_game)
    elif score.count(2) == 4 and turns_taken != 5:
        return random.choice(feedback_close_win)
    elif score.count(2) == 4 and turns_taken == 5:
        return random.choice(feedback_close_call)
    elif score.count(2) < 3 and turns_taken == 5:
        return random.choice(feedback_unlikely_win)
    else:
        logging.warning(f"No response match in give_feedback for turn {MAX_ATTEMPTS - turns_taken}")


def play():
    """Code that controls the interactive game play"""
    in_game = True

    while in_game == True:
        turns_taken = 0
        win_state = False
        score = None
        word_of_the_day = get_target_word()
        valid_words = get_valid_words()
        letter_dictionary = generate_letters()
        guesses_list = list()

        while turns_taken <= MAX_ATTEMPTS:
            remaining_turns = MAX_ATTEMPTS - turns_taken
            print(f"You have {remaining_turns} turns left\n")

            if turns_taken > 0:
                print("Here are all the letters you have left:\n")
                remaining_letters = format_remaining_letters(letter_dictionary, score, guess)
                letter_dictionary = remaining_letters[0]
                print(remaining_letters[1] + '\n')

            guess = ask_for_guess(valid_words)
            score = score_guess(guess, word_of_the_day)
            turns_taken += 1
            guesses_list.append(format_score(guess, score))
            print("Here's how close you got:\n")
            for entry in guesses_list:
                print(entry)
            print("\n")

            if is_correct(score):
                win_state = True
                break

            print(give_feedback(score, turns_taken))

            print("\n---------------------------------------------------------------------------\n")

        if win_state == True and turns_taken < MAX_ATTEMPTS:
            print(f"Congratulations! You guessed the word in {turns_taken} turns!")
        elif win_state == True and turns_taken == MAX_ATTEMPTS:
            print("Phew, that was close! You guessed it on your last chance!")
        elif win_state == False and score.count(2) > 3:
            print("Oh no! You were so close!")
        elif win_state == False and score.count(2) < 3:
            print("Look, we all have bad days. Try again whenever you feel like it and I bet you'll do great next time :)")

        exit_decision = input("Do you want to play again? Enter Y or N: ")
        if exit_decision == 'y' or exit_decision == 'Y':
            in_game = True
        elif exit_decision == 'n' or exit_decision == 'N':
            in_game = False

    # end iteration
    return True


def is_correct(score):
    """Checks if the score is entirely correct and returns True if it is
    Examples:
    >>> is_correct((1,1,1,1,1))
    False
    >>> is_correct((2,2,2,2,1))
    False
    >>> is_correct((0,0,0,0,0))
    False
    >>> is_correct((2,2,2,2,2))
    True"""

    if score == (2, 2, 2, 2, 2):
        return True
    else:
        return False


def get_valid_words(file_path=ALL_WORDS):
    """returns a list containing all valid words.
    Note to test that the file is read correctly, use:
    >>> get_valid_words()[0]
    'aahed'
    >>> get_valid_words()[-1]
    'zymic'
    >>> get_valid_words()[10:15]
    ['abamp', 'aband', 'abase', 'abash', 'abask']
    """
    # read words from files and return a list containing all words that can be entered as guesses
    all_words_handle = open(file_path)
    all_words_list = all_words_handle.readlines()
    all_words_stripped = list()
    for line in all_words_list:
        all_words_stripped.append(line.rstrip('\n'))
    return all_words_stripped


def get_target_word(file_path=TARGET_WORDS, seed=None):
    """Picks a random word from a file of words

    Args:
        file_path (str): the path to the file containing the words

    Returns:
        str: a random word from the file

    >>> get_target_word(seed=0)
    'aback'
    >>> get_target_word(seed=-1)
    'zonal'

    """

    target_words_handle = open(file_path)
    target_words_list = target_words_handle.readlines()

    if seed == None:
        target_word = random.choice(target_words_list)
    else:
        target_word = target_words_list[seed]

    return target_word.rstrip()


def ask_for_guess(valid_words):
    """Requests a guess from the user directly from stdout/in
    Returns:
        str: the guess chosen by the user. Ensures guess is a valid word of correct length in lowercase
    """
    current_guess_accepted = False
    current_guess = input("Please enter a five letter English word: ")
    current_guess = current_guess.lower()
    tomfoolery_counter = 0

    while current_guess_accepted == False:
        if tomfoolery_counter >= 5:
            current_guess = input("Are you just messing with me at this point? I just need a five letter word in English! Try again: ")
        if len(current_guess) > 5:
            tomfoolery_counter += 1
            current_guess = input("That word is too long! Try again with a five letter word: ")
        elif len(current_guess) < 5:
            tomfoolery_counter += 1
            current_guess = input("Your guess is too short! Try again with a five letter word: ")
        elif current_guess not in valid_words:
            tomfoolery_counter += 1
            current_guess = input("Sorry, that word isn't in the dictionary. Try again: ")
        else:
            current_guess_accepted = True

    return current_guess


def score_guess(guess, target_word):
    """given two strings of equal length, returns a tuple of ints representing the score of the guess
    against the target word (MISS (0), MISPLACED (1), or EXACT (2)
    Here are some examples (will run as doctest):

    >>> score_guess('hello', 'hello')
    (2, 2, 2, 2, 2)
    >>> score_guess('drain', 'float')
    (0, 0, 1, 0, 0)
    >>> score_guess('hello', 'spams')
    (0, 0, 0, 0, 0)
    >>> score_guess('gauge', 'range')
    (0, 2, 0, 2, 2)
    >>> score_guess('melee', 'erect')
    (0, 1, 0, 1, 0)
    >>> score_guess('array', 'spray')
    (0, 0, 2, 2, 2)
    >>> score_guess('train', 'tenor')
    (2, 1, 0, 0, 1)
        """

    if guess == target_word:
        return (2, 2, 2, 2, 2)

    score_list = [0, 0, 0, 0, 0]
    target_frequency = dict()
    guess_frequency = dict()

    for word_index, letter in enumerate(guess):
        target_frequency[target_word[word_index]] = target_word.count(target_word[word_index])
        if letter not in guess_frequency:
            guess_frequency[letter] = 0
        if letter == target_word[word_index]:
            score_list[word_index] = 2
            guess_frequency[letter] += 1
        elif letter not in target_word:
            score_list[word_index] = 0

    for word_index, letter in enumerate(guess):
        if letter in target_word:
            if score_list[word_index] == 2:
                continue
            elif guess_frequency[letter] < target_frequency[letter]:
                score_list[word_index] = 1
                guess_frequency[letter] += 1

    return tuple(score_list)


def help():
    """Provides help for the game"""
    pass


def format_score(guess, score):
    """Formats a guess with a given score as output to the terminal.
    The following is an example output (you can change it to meet your own creative ideas, 
    but be sure to update these examples)
    >>> print(format_score('hello', (0,0,0,0,0)))
    \033[0;40mH\033[0;40mE\033[0;40mL\033[0;40mL\033[0;40mO\033[m
    >>> print(format_score('hello', (0,0,0,1,1)))
    \033[0;40mH\033[0;40mE\033[0;40mL\033[0;43mL\033[0;43mO\033[m
    >>> print(format_score('hello', (1,0,0,2,1)))
    \033[0;43mH\033[0;40mE\033[0;40mL\033[0;42mL\033[0;43mO\033[m
    >>> print(format_score('hello', (2,2,2,2,2)))
    \033[0;42mH\033[0;42mE\033[0;42mL\033[0;42mL\033[0;42mO\033[m"""

    green = "\033[0;42m"
    yellow = "\033[0;43m"
    black = "\033[0;40m"
    reset = "\033[m"
    guess_upper = guess.upper()
    score_formatted = str()

    for counter, letter_score in enumerate(score):
        if letter_score == 2:
            score_formatted += green + guess_upper[counter]
        elif letter_score == 1:
            score_formatted += yellow + guess_upper[counter]
        elif letter_score == 0:
            score_formatted += black + guess_upper[counter]

    score_formatted += reset

    return  score_formatted


def main(test=False):
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        filename="development_log.log"
    )

    logging.debug("Test Debug message")
    logging.info("Test Info message")
    logging.warning("Test Warning message")
    logging.error("Test Error message")
    logging.critical("Test Critical message")

    #if test:
     #   import doctest
      #  print(doctest.testmod())

    play()
    exit_time = input("Thank you for playing!")



if __name__ == '__main__':
    (main(test=False))