#!/usr/bin/env python
# coding: utf-8

# In[5]:


"""A simple number guessing program"""

import random
import math


print("Welcome to the Number Guessing Game!\n")
print("Please choose your parameters so we can get started :)")

lowest_num = int(input("Please choose the minimum number: "))
highest_num = int(input("Please choose the highest number: "))

random_number = random.randint(lowest_num, highest_num)

# The amount of tries that we will give the user will depend on what range they choose.
# We will use an algorithm that will determine the max number of tries.
# log2(upper - lower + 1) will determine the amount of tries.
# Quick summary: half of 100 = 50, half of 50 = 25, half of 25 = 12.5, 
#                half of 12 = 6, half of 6 = 3, half of 3 = 1.5 
print(f"\nYou only have {round(math.log(highest_num - lowest_num + 1, 2))} tries to guess the correct number. ")

# We start with a count of 0 and then thereafter we will add 1 as tries go by
count = 0 

while count < math.log(highest_num - lowest_num + 1, 2):
    count += 1
    
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print("WOW! Well Done! You guessed the number! :)\n")
        
        # Ask the player if they want to play again
        play_prompt = input("Would you like to play again? (y/n): ")
        count = 0
        random_number = random.randint(lowest_num, highest_num)
        if play_prompt.lower() == 'n':
            print("See you next time!")
            break
    
    # Adding in tips to guess either higher or lower
    elif guess > random_number:
        print("You need to go lower!")
    elif guess < random_number:
        print("You need to go higher!")
        
if count >= math.log(highest_num - lowest_num + 1, 2):
    print("\nYou ran out of guesses :(.\n"
          f"The number that you had to guess was {random_number}")
    print("No stress... You can always play again :)")
    
        
    

