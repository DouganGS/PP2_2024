def guess_game():
    name = input('Hello! What is your name?\n')
    firstattempt = int(input(f"Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n"))
    Chinese_number = 4
    attempts = 1
    while 1:
        if firstattempt == Chinese_number:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break
        else:
            if firstattempt < Chinese_number:
                firstattempt = int(input("Your guess is too low.\nTake a guess.\n"))
            else:
                firstattempt = int(input("Your guess is too big.\nTake a guess.\n"))
                
        attempts+=1
    
guess_game()
        