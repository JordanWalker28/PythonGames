import random

def createRandomNumber():
    randomNumber = random.randint(0,100)
    return randomNumber

def computerNewGuess(lowerNumber, higherNumber):
    computerNewGuess = random.randint(lowerNumber,higherNumber)
    return computerNewGuess


def computerTurn(computerGuess, gameNumber, lowerNumber, higherNumber):

    if computerGuess == gameNumber:
        print("Computer guesses: ", computerGuess)
        print("Congratulations AI has won")
        return computerGuess
    elif computerGuess > gameNumber:
        print("AI guesses: ", computerGuess)
        higherNumber = computerGuess - 1
        print("AI guessed too high")
        computerGuess = computerNewGuess(lowerNumber, computerGuess)
        return computerGuess, lowerNumber, higherNumber
            
    elif computerGuess < gameNumber:
        lowerNumber = computerGuess + 1
        print("AI guesses: ", computerGuess)
        print("AI guessed too low")
        
        computerGuess = computerNewGuess(computerGuess, higherNumber)
        
        return computerGuess, lowerNumber, higherNumber

def playerTurn(gameNumber):
       
    guess = input("Guess the number" )
    guessNo = int(guess)
    if guessNo == gameNumber:
        print("Congratulations Player has won")
        return guess
    elif guessNo > gameNumber:
        print("You have gone too high!")
        
    elif guessNo < gameNumber:
        print("You have gone too low")
    
def gameLoop(gameNumber, computerGuess, lowerNumber, higherNumber, playerGuess):
    
    while(1):
        print(" ")
        computerGuess, lowerNumber, higherNumber = computerTurn(computerGuess,gameNumber,lowerNumber, higherNumber)
        playerGuess = playerTurn(gameNumber)
        if(playerGuess == gameNumber):
            print("Congratulations you have won")
            break            
        print(" ")
        
def game():
    
    gameNumber = createRandomNumber()
    print("GameNumber is", gameNumber)
    computerGuess = createRandomNumber()
    lowerNumber = 0
    higherNumber = 100
    playerGuess = 0

    gameLoop(gameNumber, computerGuess, lowerNumber, higherNumber, playerGuess)

game()
