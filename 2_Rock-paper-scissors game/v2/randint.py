#import random or
from random import randint

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
	elif computer =="scissors":
		print("Player one wins")

elif player == "paper": 
	if computer =="rock":
		print("Player one wins")
	elif computer =="scissors":
		print("Computer wins")

elif player == "scissors":
	if computer =="paper":
		print("Player one wins")
	elif computer =="rock":
		print("Computer wins")

else:
	print("Invalid Choice")
