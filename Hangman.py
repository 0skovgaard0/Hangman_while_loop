# Welcome to a simple game of Hangman based on a while loop.
# While you guess a character the word or words consist of,
# you're doing great and get closer to win, if you guess wrong,
# you will loose a live.

def display_current_state(lives, guess):
    print(f"You have {lives} lives left...")
    print("The secret phrase:")
    output = " ".join(guess)
    print(output)
    print("")

# Solution - Here you can customize the word "  " the user needs to guess.
solution = "Richard Branson".lower()
# Lives - Number of lives the user has
lives = 10
guess = "_" * len(solution)

# 1. Let the user guess as long as they have lives left
while lives > 0 and "_" in guess:
    display_current_state(lives, guess)
    
    # 2. Take the guess from the user
    user_input = input("Guess a character (including whitespace): ").lower()
    
    # 3. Find all indices where the guessed character occurs in the solution
    indices = [i for i, char in enumerate(solution) if char == user_input]
    
    # 4. Test whether the guessed character didn't occur -- reduce lives if so
    if not indices:
        lives -= 1
    
    # 5. Fill in the guess at all correct indices
    for index in indices:
        guess = guess[:index] + user_input + guess[index + 1:]
    
# 6. Successfull termination?   
# win_solution = solution.title()
if lives == 0:
    print("Game over!")
else:
    print(f"""\tYou won! Great job :-) 
    You guessed the solution: {solution.title()}
    """)