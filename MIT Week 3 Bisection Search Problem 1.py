# Code for a simple game that illustrates the effectiveness of binary search

print("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = (low+high)/2
print("Is your secret number " + str(guess) + "?")
user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while user_input != 'c':
    if user_input == 'l':
        low = guess
        guess = (low+high)//2
        print("Is your secret number " + str(guess) + "?")
        user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    elif user_input == 'h':
        high = guess
        guess = (low+high)//2
        print("Is your secret number " + str(guess) + "?")
        user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    else:
        print("I'm sorry, I didn't understand your input. \
              Let's try that again!")
        print("Is your secret number " + str(guess) + "?")
        user_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

print("Game over. Your secret guess was: " + str(guess))