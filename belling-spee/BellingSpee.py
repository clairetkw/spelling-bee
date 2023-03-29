from DataProcessing import answerSet, answerSetCopy, n, targetWord, targetSet, randomLetter

def bellingSpee(guess, answerSet, answerSetCopy, n, targetWord, targetSet, randomLetter):

    print("\nWelcome! To play, form words consisting of 4 or more letters by using the letters below (letters may be repeated). Each word must contain a compulsory letter (shown below).")
    print("\nYour letters are: " + targetSet)
    print("Each word must contain this letter: " + randomLetter)
    print("\nFor a hint, enter 'gimme a hint!'\nTo give up, enter 'i give up!'\n\nHappy guessing!\n")
   
    gameEnded = False
    correctGuesses = []
  

    while not gameEnded:
        if len(answerSet) == 0:
            print("\nCongratulations, you found all the words!")
            gameEnded = True
            break
        else:
            guess = input().lower()

        if guess == "i give up!":
            print("\nThe pangram was '" + targetWord + "'")
            print("The answers were: " + str(answerSetCopy))
            print("\nBetter luck next time!")
            gameEnded = True
            break
        if guess == "gimme a hint!" and len(answerSet) > 0:
            print("There are " + str(len(answerSet)) + " words left to find!\n")
        if len(guess) < 4:
            print("\nToo short\n")
        if n.search(guess) is None:
            print("\nMissing center letter\n")
        if guess not in answerSet and guess not in correctGuesses:
            print("\nNot in word list\n")
        if guess in correctGuesses:
            print("\nAlready found\n")
        if guess in answerSet:
            correctGuesses.append(guess)
            answerSet.remove(guess)
            print("\nGood job!")
            print("Words found so far: " + str(correctGuesses) + "\n")
        
bellingSpee("", answerSet, answerSetCopy, n, targetWord, targetSet, randomLetter)