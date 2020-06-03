word = "world of warcraft"

def check(wordThree):
    if "_" in wordThree:
        print("keep going sucka")
    else:
        print("You have won!") 


def update(wordThree, guess):
    count = 0
    print("letter is in word")
    for i in word:
         if guess == i:
            wordThree[count] = guess
         count = count + 1
    return wordThree

def gameLoop(word):
    seenLetters = []
    wordTwo = ""
    for char in word:
        if char == " ":
            wordTwo = wordTwo + " "
        else:
            wordTwo = wordTwo + "_"
        
    wordThree = list(wordTwo)
    guesses = 5
    print("you have " + str(guesses) + " remaining")
    while(guesses > 0):
        print("".join(wordThree))
        guess = input("guess a letter:")
        seenLetters.append(guess)
        if guess in word:
            update(wordThree, guess)
            check(wordThree)
        else:
            print("letter is not in word")
            guesses = guesses - 1
            print("you have " + str(guesses) + " remaining") 
            if(guesses == 0):
                print("You loose sucka!!")
        print(seenLetters)

gameLoop(word)
