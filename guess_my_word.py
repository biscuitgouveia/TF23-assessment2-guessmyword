import random

# TODO - List of letters guessed and not guessed at the bottom of the terminal every turn
#        - Done but lists letters which are green sometimes when there is another instance
#          of that letter in white elsewhere in the guess

# Variable declarations
MAX_TRIES = 6
attempts = 0
game_state = "in_game"
guesses = list()


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

    return (score_string + colour_reset, score_list)

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