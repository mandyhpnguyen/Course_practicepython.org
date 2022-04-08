count = 0

while True:

    import random
    import sys

    randomNum = random.randint(1, 9)
    guessNum = input("\nEnter a Number (0-9) to Guess: ")

    if guessNum == "exit" or guessNum == "e":
        print("\n> End of Program!! <\n")
        sys.exit()
        break
    elif type(int(guessNum)) == int:
        
        guessNum = int(guessNum)
        
        if randomNum == guessNum:
            print(f"You guessed exactly! We both guessed {randomNum}!!")
        elif randomNum < guessNum:
            print(f"Your number {guessNum} is larger than our number {randomNum} by the distance of {guessNum-randomNum}")
        else:
            print(f"Your number {guessNum} is smaller than our number {randomNum} by the distance of {-guessNum+randomNum}")

        count = count + 1
        print(f"Total Play Time(s): {count}")
        
        while True:
            exit_prompt = input("\nWould you like to play again? (Yes/No): ").lower()
            yesPromptList = ["y", "yes"]
            noPromptList = ["n", "no"]
            if exit_prompt in yesPromptList:
                break
            elif exit_prompt in noPromptList:
                print("\n> End of Program!! <\n")
                sys.exit()
                break
            else:
                print("Error: Try Again!!")
                continue
    else:
        print("Error: Try Again!!")