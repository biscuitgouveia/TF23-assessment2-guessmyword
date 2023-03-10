import random
import time

# Variable declarations
MAX_TRIES = 6
TARGET_WORDS = open("word-bank/all_words.txt")
VALID_WORDS = open("word-bank/target_words.txt")
attempts = 0
game_state = "in_game"

# Function definitions

# Function to choose a word for the current round
def choose_word(words):
    valid_words_list = words.readlines()
    target_word = random.choice(valid_words_list)
    return random.choice(target_word)

# TODO: Simplify the scoring algorithm. It works, but it's a bit convoluted
# Function to compare the guessed word and the target word and return a colour-formatted string
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

# Function to validate the guess as being a 5 letter English word
def validate_word(guess_word):
    if len(guess_word) < 5:
        return "Invalid - Not enough letters!"
    elif len(guess_word) > 5:
        return "Invalid - Too many letters!"
    #TODO - this doesnt work for some reason :(
    elif guess_word not in VALID_WORDS.readlines():
        return "Invalid - Word not found in the dictionary!"
    else:
        return True

# TODO: Write instructions!

print("These will be instructions my g")

while True:
    print("Selecting a word...")
    time.sleep(2)
    target_word = choose_word(VALID_WORDS)
    print("Word selected! Time to play!")

    while game_state == "in_game":
        current_guess = input("Please type a 5 letter English word: ")
        print("Checking word...")
        time.sleep(2)

        if validate_word(current_guess) != True:
            print(validate_word(current_guess))
            time.sleep(2)
            continue
        elif current_guess == target_word:
            game_state = "win"
            break
        else:
            current_guess_scored = score_word(current_guess, target_word)
            print(current_guess_scored)
            attempts += 1

        if attempts >= 6:
            game_state = "lose"
            break

    # TODO - Write this shit
    if game_state == "win":
        print("Wow gg")
    else:
        print("Lol fuck u")

    decision = input("Do you want to play again? Y or N: ")

    if decision == Y:
        continue
    else:
        break