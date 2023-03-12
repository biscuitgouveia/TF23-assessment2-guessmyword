import random

# Variable declarations
ALL_WORDS = "word-bank/all_words.txt"
TARGET_WORDS = "word-bank/target_words.txt"
MAX_TRIES = 6
attempts = 0
game_state = "in_game"
guesses = list()

# Function definitions
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

    if seed=None:
        target_word = random.choice(target_words_list)
    else:
        target_word = target_words_list[seed]

    return target_word.rstrip()

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
    return all_words_list

# Function to validate the guess as being a 5 letter English word
def validate_word(guess_word):


    if len(guess_word) < 5:
        return "Invalid - Not enough letters!"
    elif len(guess_word) > 5:
        return "Invalid - Too many letters!"

    for line in VALID_WORDS:
        if line.startswith(guess_word):
            return True
        else:
            continue

    return f"Invalid - \'{guess_word}\' is not found in the dictionary!"










'''
# TODO: Write real instructions!
print("These will be instructions my g")

while True:
    print("Selecting a word...")
    current_target = choose_word()
    print("Word selected! Time to play!")
    print(current_target)
    guessed_letters = list()

    while game_state == "in_game":
        current_guess = input("Please type a 5 letter English word: ")
        print("Checking word...")

        if validate_word(str(current_guess)) != True:
            print(validate_word(current_guess))
            continue
        elif current_guess == current_target:
            game_state = "win"
            break
        else:
            current_guess_score = score_word(current_guess, current_target)
            guesses.append(current_guess_score[0])
            for letter in current_guess_score[1]:
                if letter[0] in guessed_letters:
                    continue
                elif letter[1] == "\033[0;37m":
                    guessed_letters.append(letter[0])

            attempts += 1
            for guess in guesses:
                print(guess)
            guessed_letters.sort()
            guessed_letters_string = str()
            for letter in guessed_letters:
                letter = letter.upper()
                guessed_letters_string += f"{letter} "
            print(f"Wrong Letters: {guessed_letters_string}")

        if attempts >= 6:
            game_state = "lose"
            break

        print(f"You have {6 - attempts} guesses remaining.")

    # TODO - Write end game interaction
    if game_state == "win":
        print("Wow gg u win nice one :)")
    else:
        print("Lol fuck u, u suck")

    decision = input("Do you want to play again? Y or N: ")

    if decision == 'Y':
        game_state = "in_game"
        attempts = 0
        continue
    else:
        break
        
        '''