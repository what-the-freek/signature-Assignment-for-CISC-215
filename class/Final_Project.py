import random
def get_range():# gets the range for what to pick from
    while True:
        try:
            start=int(input("what is the starting number aka the lowest ")) #starting number
            end=int(input("what is the ending number aka the highest ")) #ending number
            if start>=end:
                print("the starting number must be lower than the ending number")
            else: 
                return start,end
        except ValueError: # if not a number must re-enter
            print("The start and End must be numbers")

def get_user_guess():#gets the guess of the player
    while True:
        try:
            return int(input("what is your guess? ")) #stores the guess
        except ValueError:
            print("Your guess must be a number")

def play_game(): #main game coding
    start,end=get_range()
    secret_number=random.randint(start,end) #picks the number
    guesses=0 #guess counter
    while True:
        try:
            guess=get_user_guess()
            guesses+=1
            if guess > secret_number:
                print("Too high!")
            elif guess < secret_number:
                print("Too Low!")
            elif guess==secret_number:
                print(f"correct you got it in {guesses} guesses ")
                break
        except ValueError:
            print("You must have a number as a guess")
            return

def play_again_or_exit():# if player wants to play again or not
    while True:
        
            play_game() #plays again
        
        
            play_again=input("would you like to play again ").strip().lower()
            if not play_again.startswith("y"):  # most confirmations start with y
                print("You are exiting, Great Job") # exits the game while giving praise
                break
        

play_again_or_exit()