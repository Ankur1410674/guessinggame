guessingGame = int(input("Guessing game (guess a number between 1-9)"))
    
random.radint(0,9)

while chances < 5:
 if guess == number:
    print("Congratulations you won!!")
 break

if not chances < 5:
    print("you lose!! the number is number")

