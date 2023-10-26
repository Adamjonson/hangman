# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variab0le wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"


    secret_word = list(secret_word)
    check = all(item in letters_guessed for item in secret_word)

    if check == True:
        return True
    else:
        return False
def get_guessed_word(secret_word, letters_guessed):

    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
    which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if not letters_guessed:
        empty_output = "_" * len(secret_word)
        return empty_output
    else:
        secret_word = list(secret_word)
        word_guessed = list()
        for sletters in secret_word:
            num_iteration = 0
            for gletters in letters_guessed:
                num_iteration += 1
                if sletters == gletters:
                    word_guessed.append(gletters)
                    break

                elif num_iteration <= (len(letters_guessed) - 1):
                    continue
                else:
                    word_guessed.append("_ ")
                    break

        output = ""
        for letter in word_guessed:
            output += letter
        return output

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # >> > letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
    # >> > print
    # get_available_letters(letters_guessed)
    # abcdfghjlmnoqtuvwxyz
    alphabet = string.ascii_lowercase


    for gletter in letters_guessed:
        for aletter in alphabet:
            if gletter == aletter:
                alphabet= alphabet.replace(gletter, "")
                break
    return alphabet



def unique_letters(secret_word):
    secret_word = list(secret_word)
    ullist = list()
    for sletter in secret_word:
        if sletter in ullist:
            continue
        else:
            ullist.append(sletter)

    return len(ullist)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass

    right_letters = list() # list for letters in a secret word
    letters_on_time = list()# to check each time if the user get the letter right
    get_letters = list()
    number_of_guesses = 6
    number_of_warnings = 3
    lvowels = ['a', 'e', 'i', 'o', 'u']
    line = "-------------------------------------------------"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long" )
    print("You have", number_of_warnings, "warning left")
    print(line)
    guess = True
    while guess:
        #print("Secret word", secret_word)
        print("Get_letters", get_letters)
        if is_word_guessed(secret_word, get_letters):
            print("Congratulations, you won!")
            total_score = number_of_guesses * unique_letters(secret_word)
            print("You total score for this game:", total_score)
            guess = False
            break
        if number_of_guesses == 0: # Terminating the game
            guess = False
            print(line)
            print("Sorry, you ran out of guesses. The word was", secret_word)
            continue

        print("You have", number_of_guesses, "guesses left")
        #print("Secret word", secret_word)
        print("Available letters:", get_available_letters(get_letters))
        letter_guessed = input("Please guess a letter: ")

        #condition to show possible words
        if letter_guessed == "*":
            show_possible_matches(get_guessed_word(secret_word, right_letters))


        # if the user input is uppercase then convert it to lowercase
        letter_guessed = letter_guessed.lower()
        # for a python to check the condition
        letters_on_time.append(letter_guessed)
        print("right letters", right_letters)
        warning_cond = True
        #if the input is not a aplhabetical value
        if not letter_guessed.isalpha() and warning_cond == True:

            if number_of_warnings == 0:
                number_of_guesses -= 1
                warning_cond = False
                letters_on_time.clear()
                continue


            if number_of_warnings == 1:
                number_of_warnings -= 1
                print("Oops! That is a not valid letter. You have", number_of_warnings, "warning left:", get_guessed_word(secret_word, right_letters))
                print(line)
                letters_on_time.clear()
            else:
                number_of_warnings -= 1
                print("Oops! That is a not valid letter. You have", number_of_warnings, "warnings left:", get_guessed_word(secret_word, right_letters))
                print(line)
                letters_on_time.clear()
            print("You can only input an alphabet letters!!!")

            continue




        print("Letters on time", letters_on_time)
        # is user input in secret word
        if any(is_letter_guessed in secret_word  for is_letter_guessed in letters_on_time):
            #If the user inputs a letter that has already been guessed
            # we subtrtract one warning
            # if no wanrings are left we substract one guess
            print("True")
            if letter_guessed in get_letters:
                print("Letters_guessed in right_letters is true")
                if warning_cond == True:

                    if number_of_warnings == 0:
                        number_of_guesses -= 1
                        warning_cond = False
                        continue
                    number_of_warnings -= 1
                    print("Oops! You have already guessed that letter. You now have", number_of_warnings, "warnings left:")
                    print(get_guessed_word(secret_word, right_letters))
                    letters_on_time.clear()
                    print(line)
                    continue
            # adding to list for letters in a secret word
            right_letters.append(letters_on_time[0])
            # the guessed letter is added to the list, so it is deleted from
            # the list of available letters
            get_letters.append(letters_on_time[0])


            print("Good guess:", get_guessed_word(secret_word, right_letters))


            letters_on_time.clear()
            print("--------------------------")
        else:
            if letter_guessed in lvowels:
                print("Oops! That letter is not in my word:")
                if number_of_guesses == 1:
                    number_of_guesses -= 2
                    continue
                print("Please guess a letter:", get_guessed_word(secret_word, right_letters))
                get_letters.append(letters_on_time[0])
                get_available_letters(get_letters)
                letters_on_time.clear()
                number_of_guesses -= 2
                print("---------------------------")
                continue
            else:
                print("Oops! That letter is not in my word:")
                if number_of_guesses == 1:
                    number_of_guesses -= 1
                    continue
                print("Please guess a letter:", get_guessed_word(secret_word, right_letters))
                get_letters.append(letters_on_time[0])
                get_available_letters(get_letters)
                letters_on_time.clear()
                number_of_guesses -= 1
                print("---------------------------")
                continue
            print("Oops! That letter is not in my word:", get_guessed_word(secret_word, right_letters))
            get_letters.append(letters_on_time[0])
            get_available_letters(get_letters)
            letters_on_time.clear()
            number_of_guesses -= 1
            if number_of_guesses == 0:
                print("Sorry, you ran out of guesses. The word was", secret_word)







# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    my_word = my_word.replace(" ", "")
    my_wordl = list(my_word)
    other_word = list(other_word)
    i = 0
    con = True
    if len(my_wordl) != len(other_word):
        con = False
        return con
    while i < len(my_wordl):
        if my_wordl[i] == "_":
            i += 1
            continue

        if my_wordl[i] == other_word[i]:
            i += 1
            continue
        else:
            con = False
            return con
    return con



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matches = list()
    for word in wordlist:
        if match_with_gaps(my_word, word) == True:
            matches.append(word)

    if matches == False:
        print("No matches found")
    else:
        for i in matches:
            print(i)
def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    right_letters = list()  # list for letters in a secret word
    letters_on_time = list()  # to check each time if the user get the letter right
    get_letters = list()
    number_of_guesses = 6
    number_of_warnings = 3

    # list of vowels to substract 2 points or one point deoending on the letter guessed line
    lvowels = ['a', 'e', 'i', 'o', 'u']


    line = "-------------------------------------------------"

    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), "letters long")
    print("You have", number_of_warnings, "warning left")
    print(line)
    guess = True
    while guess:
        #print("Secret word", secret_word)
        print("Get_letters", get_letters)


        # Stops the game if the letters are right
        if is_word_guessed(secret_word, get_letters):
            print("Congratulations, you won!")
            total_score = number_of_guesses * unique_letters(secret_word)
            print("You total score for this game:", total_score)
            guess = False
            break


        # Terminating the game
        if number_of_guesses <= 0:
            guess = False
            print(line)
            print("Sorry, you ran out of guesses. The word was", secret_word)
            continue


        print("You have", number_of_guesses, "guesses left")
        #print("Secret word", secret_word)
        print("Available letters:", get_available_letters(get_letters))
        letter_guessed = input("Please guess a letter: ")


        # condition to show possible words
        if letter_guessed == "*":
            show_possible_matches(get_guessed_word(secret_word, right_letters))
            print(line)
            continue


        # if the user input is uppercase then convert it to lowercase
        letter_guessed = letter_guessed.lower()



        letters_on_time.append(letter_guessed)


        print("right letters", right_letters)
        warning_cond = True


        # if the input is not a aplhabetical value
        if not letter_guessed.isalpha() and warning_cond == True:

            # in case if the no warnings left
            if number_of_warnings == 0:
                number_of_guesses -= 1
                warning_cond = False
                letters_on_time.clear()
                print(line)
                continue

            else:
                number_of_warnings -= 1
                print("Oops! That is a not valid letter. You have", number_of_warnings, "warning left:",
                      get_guessed_word(secret_word, right_letters))
                print(line)
                letters_on_time.clear()

            # if number_of_warnings == 1:
            #     number_of_warnings -= 1
            #     print("Oops! That is a not valid letter. You have", number_of_warnings, "warning left:",
            #           get_guessed_word(secret_word, right_letters))
            #     print(line)
            #     letters_on_time.clear()
            # else:
            #     number_of_warnings -= 1
            #     print("Oops! That is a not valid letter. You have", number_of_warnings, "warnings left:",
            #           get_guessed_word(secret_word, right_letters))
            #     print(line)
            #     letters_on_time.clear()
            print("You can only input an alphabet letters!!!")

            continue

        print("Letters on time", letters_on_time)
        # is user input in secret word
        if any(is_letter_guessed in secret_word for is_letter_guessed in letters_on_time):
            # If the user inputs a letter that has already been guessed
            # we subtrtract one warning
            # if no wanrings are left we substract one guess
            print("True")
            if letter_guessed in get_letters:
                print("Letters_guessed in right_letters is true")
                if warning_cond == True:

                    if number_of_warnings == 0:
                        number_of_guesses -= 1
                        warning_cond = False
                        continue
                    number_of_warnings -= 1
                    print("Oops! You have already guessed that letter. You now have", number_of_warnings,
                          "warnings left:")
                    print(get_guessed_word(secret_word, right_letters))
                    letters_on_time.clear()
                    print(line)
                    continue
            # adding to list for letters in a secret word
            right_letters.append(letters_on_time[0])
            # the guessed letter is added to the list, so it is deleted from
            # the list of available letters
            get_letters.append(letters_on_time[0])

            print("Good guess:", get_guessed_word(secret_word, right_letters))

            letters_on_time.clear()
            print("--------------------------")
        else:
            if letter_guessed in lvowels:
                print("Oops! That letter is not in my word:")
                if number_of_guesses == 1:
                    number_of_guesses -= 2
                    continue
                print("Please guess a letter:", get_guessed_word(secret_word, right_letters))
                get_letters.append(letters_on_time[0])
                get_available_letters(get_letters)
                letters_on_time.clear()
                number_of_guesses -= 2
                print("---------------------------")
                continue
            else:
                print("Oops! That letter is not in my word:")
                if number_of_guesses == 1:
                    number_of_guesses -= 1
                    continue
                print("Please guess a letter:", get_guessed_word(secret_word, right_letters))
                get_letters.append(letters_on_time[0])
                get_available_letters(get_letters)
                letters_on_time.clear()
                number_of_guesses -= 1
                print("---------------------------")
                continue


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
