
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