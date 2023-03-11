import random

# TODO - List of letters guessed and not guessed at the bottom of the terminal every turn
# TODO - Stack of previous guesses like in real Wordle
# TODO - Counter for how many turns left

# Variable declarations
MAX_TRIES = 6
attempts = 0
game_state = "in_game"


# Function definitions
# Function to choose a word for the current round
def choose_word():
    TARGET_WORDS = open("word-bank/target_words.txt")
    target_words_list = TARGET_WORDS.readlines()
    target_word = random.choice(target_words_list)
    return target_word.rstrip()

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
    colour_reset = "\u001b[0m"

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

    return score_string + colour_reset

# Function to validate the guess as being a 5 letter English word
def validate_word(guess_word):
    VALID_WORDS = open("word-bank/all_words.txt")

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

# TODO: Write real instructions!
print("These will be instructions my g")

while True:
    print("Selecting a word...")
    current_target = choose_word()
    print("Word selected! Time to play!")
    print(current_target)

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
            print(score_word(current_guess, current_target))
            attempts += 1

        if attempts >= 6:
            game_state = "lose"
            break

    # TODO - Write end game interaction
    if game_state == "win":
        print("Wow gg u win nice one :)")
    else:
        print("Lol fuck u, u suck")

    decision = input("Do you want to play again? Y or N: ")

    if decision == 'Y':
        game_state = "in_game"
        continue
    else:
        break