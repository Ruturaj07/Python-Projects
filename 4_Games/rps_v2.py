#import random or
from random import randint
player_score = 0
computer_score = 0
winning_score = 3

while player_score < winning_score and computer_score < winning_score :
	print(f"Player score {player_score} Computer score {computer_score}")
	print("....rock....")
	print("....paper....")
	print("....scissors....")

	player = input("Player, enter your choice :").lower()

	ran_num = randint(0,2)
	if ran_num == 0:
		computer = "rock"
	elif ran_num == 1:
		computer = "paper"
	else :
		computer = "scissors"
	print(f"Computer plays {computer}")

	if player == computer :
		print("Its a Tie!!")

	elif player == "rock": 
		if computer =="paper":
			print("Computer wins")
			computer_score +=1
		elif computer =="scissors":
			print("Player one wins")
			player_score += 1

	elif player == "paper": 
		if computer =="rock":
			print("Player one wins")
			player_score += 1
		elif computer =="scissors":
			print("Computer wins")
			computer_score +=1

	elif player == "scissors":
		if computer =="paper":
			print("Player one wins")
			player_score += 1
		elif computer =="rock":
			print("Computer wins")
			computer_score +=1

	else:
		print("Invalid Choice")

if player_score > computer_score:
	print("Player wins, yeepiee!!")
elif player_score == computer_score:
	print("Its a Tie")
else:
	print("Oh no, Computer won the war!!")
