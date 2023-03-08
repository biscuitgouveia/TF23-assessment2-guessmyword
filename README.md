# TF23-assessment2-guessmyword
Guess My Word Assessment

### Scoring Algorithm
#### Rules:
* Letters matching and in the correct place will be formatted green
* Letters matching and in the wrong place will be formatted yellow
* Letters which do not match any in the target word will be formatted white
* If there are more instances of a letter in the target word than in the guessed word, the letter(s) will be formatted yellow or green as appropriate and no other indication will be given of extra missing letters until that letter is included in a further guess
* If there are more instances of a letter in the guess word than in the target word, they will be formatted as follows:
  * Any letters in the correct place will be formatted green first
  * If there are any more of the letter in the target word but they are in the wrong place in the guessed word, they will be formatted yellow
  * If the number of formatted letters in the guess word is equal to the number of instances of that letter in the target word, any remaining instances of that letter in the guess word will be formatted as white

#### Pseudocode

```angular2html
score_word(guess_word, target_word):

  score_string = empty string
  score_list = empty list
  target_frequency = empty dictionary
  guess_frequency = empty dictionary
  green = "\033[0;32m" (ANSI Code for Green Text)
  yellow = "\033[0;33m" (ANSI Code for Yellow Text)
  white = "\033[0;37m" (ANSI Code for White Text)

  for each letter in guess_word:
    append a tuple of (letter, white) to score_list
  for each letter in target_word:
    create key-value pairs in target_frequency of 
    {each letter: # of occurences}
  for each letter in guess_word:
    create key-value pairs in guess_frequency of
    {each letter: 0}

  for each letter in guess_word:
    if the letter matches and is in the right place:
      set score_list at this index to (letter: green) +1 frequency of this letter in guess_frequency

  for each letter in guess_word:
    if this index in score_list is (letter, green):
      skip this letter and start next iteration
    else:
      +1 frequency of this letter in guess_frequency
    
    if letter exists in target_word AND has appeared so far <= to the amount of times in the target word:
      set score_list at this index to (letter: yellow)
    else:
      set score_list at this index to (letter: white)

  for each tuple in score_list:
    add colour+letter to score_string
  
  return score_string
```

#### Code

```angular2html
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
```