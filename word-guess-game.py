import random
#TODO: Create a list of words
word = random.choice(["RECURSION", "ITERATION", 'CONDITIONS', 'PROGRAMMING', 'VARIABLES'])
#TODO: Convert the word to uppercase and strip the spaces
word = word.strip().upper()

#TODO: Create a list of letters of the word and save the length of the word
lenOfWord = len(word)
letterListOfTheWord= list(word)

#TODO: Create a list of the word in underline format and save it as a list
wordInUnderlineformat = word[0] + ' ' * (len(word) - 1)
listOfUnderlineFormat = list(wordInUnderlineformat)

def startProgram():
    #TODO: Initialize the variables
    totalPoints = 12
    limitOfLettersToPurchase = 4
    limitOfGuesses = 3
    validChoices = [1,2]
    isUserWon = False
    alreadyPurchasedLetters =[]
    
    #TODO: Print the welcome message and the rules of the game
    print('Word Prediction Game')
    print('-------')
    print(f'The word has {lenOfWord} letters.')
    print(f'You have {totalPoints} points in total to start with.')
    print('You can buy a letter at a cost of 2 points.')
    print('You can buy 4 letters at max.')
    print('You can make a guess at max 3 times.')
    print('Each wrong guess results in 2 points loss.')
    
    #? Check if the user can continue to the game
    while (isUserWon == False) and (limitOfGuesses > 0 ) and (totalPoints > 0):
        print(f'\n***Remaining points: {totalPoints}***')    
        print('\n1. Make a guess')
        print('2. Buy a letter\n')
        try:
            roundChoice = int(input('What to do: '))
            if (roundChoice not in validChoices):
                print('\nWARNING: Please enter 1 or 2. \n')
            else: 
                #* 1: Make a guess
                if (roundChoice == 1):
                    while True:
                        try:
                            guess = str(input('Make your guess: ')).strip().upper()
                            #? Check if the guess is correct
                            if(guess == word):
                                print('\nCORRECT! You won!')
                                print(f'Your points: {totalPoints} ') 
                                isUserWon = True   
                                break
                            #? Check if the guess is incorrect
                            else: 
                                print('\nIncorrect guess!\n')
                                totalPoints -= 2
                                limitOfGuesses -= 1
                                break
                        except:
                            print('Invalid input. Please enter a string value.')
                
                
                #* 2: Purchase a letter
                elif (roundChoice == 2):
                    #? Check if the user can buy a letter
                    if (limitOfLettersToPurchase == 0):
                        print('You cannot buy more letters.')
                    #? Check if the user has enough points to buy a letter
                    elif (totalPoints == 2):
                        print('You cannot buy a letter.')
                        print('Otherwise, the game will end.')
                    
                    else:
                        limitOfLettersToPurchase -= 1
                        totalPoints -= 2
                        purchasedLetter = random.choice(letterListOfTheWord)
                        #? Check if the letter is already purchased
                        while (purchasedLetter in alreadyPurchasedLetters):
                            purchasedLetter = random.choice(letterListOfTheWord)
                            if (purchasedLetter not in alreadyPurchasedLetters):
                                break 
                        print(f'\nThe letter purchased is {purchasedLetter}')
                        
                        #TODO: Update the underline format of the word with the purchased letter
                        for letter in letterListOfTheWord:
                            #? check if the letter is the purchased letter and not in the already purchased letters list
                            if((letter == purchasedLetter) and (letter not in alreadyPurchasedLetters)):
                                ixOfPurchasedLetter = word.index(purchasedLetter)
                                listOfUnderlineFormat.pop(ixOfPurchasedLetter)
                                alreadyPurchasedLetters.append(letterListOfTheWord[ixOfPurchasedLetter])
                                listOfUnderlineFormat.insert(ixOfPurchasedLetter, letter) 
                        
                        #TODO: Print the updated underline format of the word
                        revealed_word = ''
                        for i in range(len(word)):
                            if letterListOfTheWord[i] in alreadyPurchasedLetters:
                                revealed_word += letterListOfTheWord[i] + ' '
                            else:
                                revealed_word += '_ '
                        print(revealed_word + '\n')
        except:
            print('\nERROR: Invalid input. Please enter 1 or 2.\n')

    print('Game over.')
    #? Check if the user finished their guesses or points
    if (limitOfGuesses == 0):
        print('You finished your guesses.')
    elif (totalPoints == 0):
        print('No points left.')
    print(f'The answer is {word}')
        
startProgram()