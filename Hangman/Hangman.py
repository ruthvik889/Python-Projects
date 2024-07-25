#Hangman

import random
#creating picture with ASCII art

HANGMAN_PICS = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    0   |
        |
        |
       ===''', '''
    +---+
    0   |
    |   |
        |
       ===''', '''
    +---+
    0   |
   /|   |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +---+
    0   |
   /|\  |
        |
       ===''', '''
    +===+
    0   |
   /|\  |
   /    |
       ===''', '''
    +---+
    0   |
   /|\  |
   / \  |
       ===''']

word_list = 'aardvark antelope baboon badger bat bear beaver buffalo camel cheetah chimpanzee coyote deer dolphin elephant ferret fox giraffe gorilla hedgehog hippopotamus hyena jaguar kangaroo koala lemur lion llama meerkat moose narwhal ocelot octopus otter panda parrot penguin platypus porcupine rabbit raccoon rhinoceros salamander seal sloth squirrel tiger tortoise toucan walrus weasel whale wolf zebra butterfly cheetah donkey eagle flamingo jellyfish lizard mosquito ostrich panther peacock seahorse skunk spider starfish swan turkey vulture'.split()

def GetRandomWord(wordList):
    word_Index = random.randint(0, len(wordList) - 1)
    return wordList[word_Index]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end = ' ')
    for letter in missedLetters:
        print(letter, end = ' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)):
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end = ' ')
    print()

def getGuess(alreadyGuessed):
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N\nThe category is animals.')
missedLetters = ''
correctLetters = ''
secretWord = GetRandomWord(word_list)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    guess = getGuess(missedLetters + correctLetters)
    if guess in secretWord:
        correctLetters += guess

        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break

        if foundAllLetters:
            print(f"Yes! The secret word is {secretWord}. You have won!")
            gameIsDone = True

    else:
        missedLetters += guess

        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord = GetRandomWord(word_list)
        else:
            break