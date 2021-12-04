from replit import clear
from random import randint
from art import logo2

clear()
GAME_LEVEL_EASY = 10
GAME_LEVEL_HARD = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == "easy":
    return GAME_LEVEL_EASY
  else:
    return GAME_LEVEL_HARD
	
def game():
	print(logo2)
	#Choosing a random number between 1 and 100.
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")
	answer = randint(1, 100)
	#print(f"Pssst, the correct answer is {answer}") 

	turns = set_difficulty()
	#Repeat the guessing functionality if they get it wrong.
	guess = 0
	while guess != answer:
		print(f"You have {turns} attempts remaining to guess the number.")

		#Let the user guess a number.
		guess = int(input("Make a guess: "))

		#Track the number of turns and reduce by 1 if they get it wrong.
		turns = check_answer(guess, answer, turns)
		if turns == 0:
			print("You've run out of guesses, you lose.")
			print(f"Pssst, the correct answer is {answer}")
			return
		elif guess != answer:
			print("Guess again.")

play_again = True
while play_again:
	game()
	reply = input("Do you want play again: \'y\' or \'n\'? ").lower()
	if reply == 'n':
		print("\nGood man, thank you for playing our game. \nWe welcome your feedback and comment to chinwej.obiageri@gmail.com. \n~ Shepherd.")
		play_again = False
	elif reply != 'y':
		reply = input("Try again: Choose \'y\' or \'n\'? ").lower()
		if reply == 'n':
			print("\nGood man, thank you for playing our game. \nWe welcome your feedback and comment to chinwej.obiageri@gmail.com. \n~ Shepherd.")
			play_again = False
	if reply == 'y':
		clear()
