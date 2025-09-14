# Exercise 0: Example
#
# This is a practice exercise to help you understand how to write code "inside" a provided Python function.
#
# We'll create a function that checks a condition and prints a specific greeting message based on that condition.
#
# Requirements:
# - The function is named `print_greeting`.
# - Inside the function, declare a variable `python_is_fun` and set it to `True`.
# - Use a conditional statement to check if `python_is_fun` is `True`.
# - If `python_is_fun` is `True`, print the message "Python is fun!"

# SAMPLE EXERCISE 0 - to show and start how to use this
def print_greeting():
    # Your code goes here. Remember to indent!
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

# Call the function
print_greeting()

#-----------------------------------------------------------------------------------

# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.


def check_letter():
    # Your control flow logic goes here
    # Asking the user to type one letter
    letter = input("Type one letter (like a or A): ")
    
    # Making the letter lowercase so don't have to check uppercase too
    letter = letter.lower()
    
    # Checking if the letter is one character long
    # Counting letters by comparing to a single letter like 'a'
    if letter == '' or letter > 'z' or letter < 'a':
        print("Type one letter from a to z.")
    else:
        # Checking if the letter is a vowel (a, e, i, o, u)
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            print("The letter", letter, "is a vowel.")
        else:
            print("The letter", letter, "is a consonant.")

# Call the function
check_letter()

#-----------------------------------------------------------------------------------

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    # Your control flow logic goes here
    # Asking user to type their age
    age_input = input("Please enter your age: ")
    
    # Turning the input into a number
    try:
        age = int(age_input)
        
        # Checking if age is negative
        if age < 0:
            print("Error: Age cannot be negative. Try again.")
        else:
            # Setting voting age to 18
            voting_age = 18
            
            # Checking if user can vote
            if age >= voting_age:
                print("You are old enough to vote.")
            else:
                print("You are not old enough to vote.")
                
    # If input is not a number, then show error
    except:
        print("Error: Enter a number.")
        
# Call the function
check_voting_eligibility()

#-----------------------------------------------------------------------------------

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.


def calculate_dog_years():
    # Your control flow logic goes here
    # Asking user to type in the dog's age
    age_input = input("Input a dog's age: ")
    
    # Trying to turn the input into a number
    try:
        age = int(age_input)
        
        # Checking if age is negative
        if age < 0:
            print("Error: Age cannot be negative. Try again.")
        else:
            # Calculating dog years
            if age <= 2:
                dog_years = age * 10  # First 2 years = 10 dog years
            else:
                dog_years = 20 + (age - 2) * 7  # So 20 for first 2 years, then after 7 per year.
            
            # Printing the result
            print("The dog's age in dog years is", dog_years, ".")
                
    # If the input is not a number, then show an error.
    except:
        print("Error: Please enter a number.")
        
# Call the function
calculate_dog_years()

#-----------------------------------------------------------------------------------

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.


def weather_advice():
    # Your control flow logic goes here
    # Asking if it is cold
    cold = input("Is it cold (yes/no)? ")
    # Asking if it is raining
    raining = input("Is it raining (yes/no)? ")
    
    # Making inputs lowercase to check more easily
    cold = cold.lower()
    raining = raining.lower()
    
    # Checking conditions and then give advice via print
    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    if cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    if cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    if cold == "no" and raining == "no":
        print("Wear light clothing.")
        
# Call the function
weather_advice()

#-----------------------------------------------------------------------------------

# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.


def determine_season():
    # Your control flow logic goes here
    # Asking for month and day
    month = input("Enter the month of the year (Jan - Dec): ")
    day_input = input("Enter the day of the month: ")
    
    # Making month lowercase
    month = month.lower()
    
    # Trying to turn day into a number
    try:
        day = int(day_input)
        
        # Checking if day is valid (1 to 31)
        if day < 1 or day > 31:
            print("Error: Day must be between 1 and 31!")
        else:
            # Checking month and day to find season
            if month == "dec" and day >= 21 or month == "jan" or month == "feb" or month == "mar" and day <= 19:
                print(month, day, "is in Winter.")
            elif month == "mar" and day >= 20 or month == "apr" or month == "may" or month == "jun" and day <= 20:
                print(month, day, "is in Spring.")
            elif month == "jun" and day >= 21 or month == "jul" or month == "aug" or month == "sep" and day <= 21:
                print(month, day, "is in Summer.")
            elif month == "sep" and day >= 22 or month == "oct" or month == "nov" or month == "dec" and day <= 20:
                print(month, day, "is in Fall.")
            else:
                print("Error: Invalid month!")
                
    # If day is not a number
    except:
        print("Error: Day must be a number!")
        
# Call the function
determine_season()

#-----------------------------------------------------------------------------------

# Exercise 6: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.


def guess_number():
    # Your control flow logic goes here
    # Setting the target number
    target = 42
    
    # Allowing 5 guesses
    for attempt in range(1, 6):
        # Asking for a guess - 1st guess
        guess_input = input("Guess a number between 1 and 100: ")
        
        # Trying to turn guess into a number
        try:
            guess = int(guess_input)
            
            # Checking if guess is valid (1 to 100)
            if guess < 1 or guess > 100:
                print("Error: Guess must be between 1 and 100.")
            else:
                # Checking if it's the last chance
                if attempt == 5 and guess != target:
                    print("Last chance!")
                    print("Sorry, you failed to guess the number in five attempts.")
                    return
                
                # Checking the guess
                if guess == target:
                    print("Congratulations, you guessed correctly. Woot woot!")
                    return
                elif guess < target:
                    print("Your guess is too low.")
                else:
                    print("Your guess is too high.")
                    
        # If guess is not a number, print error message.
        except:
            print("Error: Please enter a number!")
            
# Call the function
guess_number()


#-----------------------------------------------------------------------------------