import random

#Guessing Game
print("\nWelcome to the Guessing Game!")
a=random.randint(1,10)

user_input = int(input("\nEnter your guess (1-10): " ))

for i in range(2):
    if user_input < a:
        print("\nToo low! Try again.")
        user_input = int(input("\nEnter your guess (1-10): " ))
    elif user_input > a:
        print("\nToo high! Try again.")
        user_input = int(input("\nEnter your guess (1-10): " ))
    else:
        print("\nCongratulations! You guessed correctly.")
        print("\nGame over!")
        exit()

print("\nWrong. You have reached the maximum number of attempts")
print("\nGame over!")