secret = 7

while True:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")