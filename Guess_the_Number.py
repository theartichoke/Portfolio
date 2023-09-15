import random

gamemode = input("Who would you like to guess the number, me? (c) or you? (p)")

if(gamemode == "p"):

    def guess(x):
        random_number = random.randint(1, x)
        guess = 0
        while guess != random_number:
            guess = int(input(f"Guess a number between 1 and {x}: "))
            print(guess)
            if guess < random_number:
                print("Too Low")
            elif guess > random_number:
                print("Too High")
        print(f"You got it!! the number was {random_number}")
    guess(int(input("What would you like the highest possible guess to be? ")))

elif(gamemode == "c"):
    def computer_guess(x):
        low = 1
        high = x
        feedback = ''
        while feedback != "c":
            if low != high:
                guess = random.randint(low, high)
            else:
                guess = low
            feedback = input(f"Was {guess} too high (h), too low (l), or right on?? ")
            if feedback == "h":
                high = guess - 1
            elif feedback == "l":
                low = guess + 1
        print(f"Yay i guessed your number!! It was {guess}")
    computer_guess(int(input("What would you like the highest possible guess to be? ")))


            

