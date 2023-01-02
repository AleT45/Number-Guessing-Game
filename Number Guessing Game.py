import random

print("Welcome to the number guessing game!")
name = input("What is your name? ")

while True:
    target_number = random.randint(1, 100)
    min_value = 1
    max_value = 100
    num_guesses = 0
    while True:
        hint = f"The number is between {min_value} and {max_value}"
        guess = int(input(f"Enter a guess ({hint}): "))
        num_guesses += 1
        if guess < target_number:
            min_value = max(min_value, guess)
        elif guess > target_number:
            max_value = min(max_value, guess)
        else:
            print(f"Congratulations, {name}! You guessed the correct number in {num_guesses} guesses.")
            break
    play_again = input("Do you want to play again, " + name + "?" "(y/n) " )
    if play_again.lower() == 'y':
        print("Let's go!")
    else:
        print("Thanks for playing," + name + "!")
        break
